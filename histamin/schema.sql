-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS food_group;
DROP TABLE IF EXISTS food;

CREATE TABLE food_group (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  group_name TEXT UNIQUE NOT NULL
);

CREATE TABLE food (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  compatibility_rating INTEGER NOT NULL,
  trigger_mechanism INTEGER NOT NULL,
  FOREIGN KEY (group_id) REFERENCES food_group (id)
);

INSERT INTO food_group (ID,group_name) VALUES (1, 'Eggs');
INSERT INTO food_group (ID,group_name) VALUES (2, 'Dairy Products');
INSERT INTO food_group (ID,group_name) VALUES (3, 'Meat');
INSERT INTO food_group (ID,group_name) VALUES (4, 'Fish');
INSERT INTO food_group (ID,group_name) VALUES (5, 'Sea Food');
INSERT INTO food_group (ID,group_name) VALUES (6, 'Starch Suppliers');
INSERT INTO food_group (ID,group_name) VALUES (7, 'Nuts');
INSERT INTO food_group (ID,group_name) VALUES (8, 'Fats and Oils');
INSERT INTO food_group (ID,group_name) VALUES (9, 'Vegetables');
INSERT INTO food_group (ID,group_name) VALUES (10, 'Herbs');
INSERT INTO food_group (ID,group_name) VALUES (11, 'Fruits');
INSERT INTO food_group (ID,group_name) VALUES (12, 'Seeds');
INSERT INTO food_group (ID,group_name) VALUES (13, 'Mushrooms');
INSERT INTO food_group (ID,group_name) VALUES (14, 'Sweeteners');
INSERT INTO food_group (ID,group_name) VALUES (15, 'Spices and Seasoning');
INSERT INTO food_group (ID,group_name) VALUES (16, 'Water');
INSERT INTO food_group (ID,group_name) VALUES (17, 'Alcoholic Beverages');
INSERT INTO food_group (ID,group_name) VALUES (18, 'Tea and Herbal Infusions');
INSERT INTO food_group (ID,group_name) VALUES (19, 'Juices');
INSERT INTO food_group (ID,group_name) VALUES (20, 'Drinks containing caffeine');
INSERT INTO food_group (ID,group_name) VALUES (21, 'Colorants');
INSERT INTO food_group (ID,group_name) VALUES (22, 'Preservatives');
INSERT INTO food_group (ID,group_name) VALUES (23, 'Flavour enhancers');
INSERT INTO food_group (ID,group_name) VALUES (24, 'Thickeners');
INSERT INTO food_group (ID,group_name) VALUES (25, 'Leavening agents');
INSERT INTO food_group (ID,group_name) VALUES (26, 'Acidifiers');
INSERT INTO food_group (ID,group_name) VALUES (27, 'Flavourings');
INSERT INTO food_group (ID,group_name) VALUES (28, 'Vitamins');
INSERT INTO food_group (ID,group_name) VALUES (29, 'Stimulants');
INSERT INTO food_group (ID,group_name) VALUES (30, 'Preparations');