from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from histamin.db import get_db

bp = Blueprint("food", __name__)


@bp.route("/")
def index():
    """Show all the foods"""
    db = get_db()
    foods = db.execute(
        "SELECT fg.group_name, f.id, f.name, f.compatibility_rating, f.trigger_mechanism"
        " FROM food_group fg JOIN food f ON fg.id = f.group_id"
    ).fetchall()
    return render_template("food/index.html", foods=foods)


def get_food(id):
    """Get a food

    Checks that the id exists
    :param id: id of food to get
    :return: the post with author information
    :raise 404: if a food with the given id doesn't exist
    """
    food = (
        get_db().execute(
            "SELECT id, group_id, name, compatibility_rating, trigger_mechanism"
            " FROM food WHERE id = ?",
            (id,),
        ).fetchone()
    )
    if food is None:
        abort(404, "Food id {0} doesn't exist.".format(id))

    return food


@bp.route("/create", methods=("GET", "POST"))
def create():
    """Create a new post for the current user."""
    if request.method == "POST":
        group = request.form["group"]
        name = request.form["name"]
        rating = request.form["rating"]
        trigger = request.form["trigger"]
        error = None

        if not name:
            error = "Name is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO food (group_id, name, compatibility_rating, trigger_mechanism)" " VALUES (?, ?, ?, ?)",
                (group, name, rating, trigger),
            )
            db.commit()
            return redirect(url_for("food.index"))

    db = get_db()
    groups = db.execute(
        "SELECT id, group_name FROM food_group "
    ).fetchall()

    compatibility_rating_list = [(-1, 'Unknown'), (0, 'Compatible'), (1, 'Slightly incompatible'), (2, 'Incompatible'),
                                 (3, 'Severely incompatible')]
    trigger_mechanism_list = [('', ''), ('H', 'Contains Histamine'), ('H!', 'Perishable, Histamine Increases'),
                              ('A', 'Contains other biogenic amines'), ('L', 'Histamine Liberator'), ('B', 'Blocks DAO')]

    return render_template("food/create.html", groups=groups, cr_list=compatibility_rating_list,
                           tm_list=trigger_mechanism_list)


@bp.route("/update/<int:id>", methods=("GET", "POST"))
def update(id):
    """Update a post if the current user is the author."""
    if request.method == "POST":
        group = request.form["group"]
        food_name = request.form["name"]
        compatibility_rating = request.form["rating"]
        trigger_mechanism = request.form["trigger"]
        error = None

        if not food_name:
            error = "Name is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "UPDATE food SET group_id= ?, name = ?, compatibility_rating = ? WHERE trigger_mechanism = ?",
                (group, food_name, compatibility_rating, trigger_mechanism)
            )
            db.commit()
            return redirect(url_for("food.index"))

    db = get_db()
    food = get_food(id)

    groups = db.execute(
        "SELECT id, group_name FROM food_group "
    ).fetchall()

    compatibility_rating_list = [(-1, 'Unknown'), (0, 'Compatible'), (1, 'Slightly incompatible'), (2, 'Incompatible'),
                                 (3, 'Severely incompatible')]

    trigger_mechanism_list = [('', ''), ('H', 'Contains Histamine'), ('H!', 'Perishable, Histamine Increases'),
                              ('A', 'Contains other biogenic amines'), ('L', 'Histamine Liberator'),
                              ('B', 'Blocks DAO')]

    return render_template("food/update.html", food=food, groups=groups, original_group=food[1],
                           cr_list=compatibility_rating_list, original_rating=food[3],
                           tm_list=trigger_mechanism_list, original_trigger=food[4])


@bp.route("/delete/<int:id>", methods=("GET", "POST"))
def delete(id):
    """Delete a post.

    Ensures that the post exists and that the logged in user is the
    author of the post.
    """
    get_food(id)
    db = get_db()
    db.execute("DELETE FROM food WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for("food.index"))
