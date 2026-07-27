-- SQLite

ALTER TABLE products
    ADD category_id INTEGER;

ALTER TABLE products
    RENAME COLUMN name TO product_name;

CREATE TABLE categories_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(10) UNIQUE NOT NULL,
    description TEXT
);

INSERT INTO categories_new (id, name, description)
    SELECT id, name, description
    FROM categories;

DROP TABLE categories;

ALTER TABLE categories_new
    RENAME TO categories;