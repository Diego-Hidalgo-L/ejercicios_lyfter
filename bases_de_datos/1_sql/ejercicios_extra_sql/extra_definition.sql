-- SQLite

INSERT INTO categories
    VALUES (1, 'Laptop', 'Portable personal computer that integrates a screen, keyboard, pointing device, and battery into a single clamshell unit.');

INSERT INTO categories
    VALUES (2, 'Smartphone', 'Handheld mobile device that combines traditional cellular phone functions with advanced computing capabilities.');

INSERT INTO categories
    VALUES (3, 'Tablet', 'Mobile computer that features a flat touchscreen as its primary interface and is typically used for browsing the internet, reading, and streaming media.');

UPDATE products SET
    category_id = 2
    WHERE id = 1;

UPDATE products SET
    category_id = 3
    WHERE id = 2;

UPDATE products SET
    category_id = 1
    WHERE id = 3;

INSERT INTO categories
    VALUES (4, 'Speaker', 'Device that converts electrical signals into sound waves.');

INSERT INTO categories
    VALUES (5, 'Car', 'Self-propelled motor vehicle designed primarily for personal road transport.');

INSERT INTO products
    VALUES (4, 998511, 'Hilux', 64589.99, '2026-01-05', 'Toyota', 3, 5);

INSERT INTO products
    VALUES (5, 741584, 'Land Cruiser Prado', 86589.99, '2026-01-5', 'Toyota', 7, 5);

INSERT INTO products
    VALUES (6, 655235, 'Stanmore IV Black', 429.99, '2026-03-01', 'Marshall', 10, 4);

INSERT INTO products
    VALUES (7, 655236, 'Stanmore IV Cream', 429.99, '2026-03-01', 'Marshall', 17, 4);

INSERT INTO products
    VALUES (8, 655237, 'Woburn III Black', 599.99, '2026-03-01', 'Marshall', 5, 4);

INSERT INTO products
    VALUES (9, 655238, 'Woburn III Brown', 599.99, '2026-03-01', 'Marshall', 7, 4);

INSERT INTO products
    VALUES (10, 741585, 'Land Cruiser Station Wagon', 169989.99, '2026-01-5', 'Toyota', 2, 5);

INSERT INTO products
    VALUES (11, 48876, 'MacBook Air', 1299.99, '2026-03-09', 'Apple', 2, 1);