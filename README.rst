Install
-------

    # clone the repository
    $ git clone https://github.com/mehmetsezgin/histamin.git
    $ cd histamin
    $ git checkout master

Create a virtualenv and activate it::

    $ python3 -m venv venv
    $ . venv/bin/activate

Install Histamin::

    $ pip install -e .

Run
---
    $ export FLASK_APP=histamin
    $ export FLASK_ENV=development
    $ flask init-db
    $ flask run

Open http://127.0.0.1:5000 in a browser.


