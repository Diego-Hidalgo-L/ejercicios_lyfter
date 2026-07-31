-- SQLite

-- Customers table:
INSERT INTO customers
    VALUES (1, 'Alice', '123-456-7890');

INSERT INTO customers
    VALUES (2, 'Bob', '981-654-3210');

INSERT INTO customers
    VALUES (3, 'Claire', '555-123-4567');


-- Addresses table:
INSERT INTO addresses
    VALUES (1, '123 Main St', 1);

INSERT INTO addresses
    VALUES (2, '456 Elm St', 2);

INSERT INTO addresses
    VALUES (3, '4th Avenue', 2);

INSERT INTO addresses
    VALUES (4, '789 Oak St', 3);

INSERT INTO addresses
    VALUES (5, '464 Georgia St', 3);


-- Items table:
INSERT INTO items
    VALUES (101, 'Cheeseburger', 8);

INSERT INTO items
    VALUES (102, 'Fries', 3);

INSERT INTO items
    VALUES (103, 'Pizza', 12);

INSERT INTO items
    VALUES (105, 'Salad', 6);

INSERT INTO items
    VALUES (106, 'Water', 1);


-- Orders table:
INSERT INTO orders
    VALUES (001, 1, 1, 19, '2026-07-27 18:00:00');

INSERT INTO orders
    VALUES (002, 2, 2, 12, '2026-07-27 19:30:00');

INSERT INTO orders
    VALUES (003, 2, 3, 6, '2026-07-27 19:30:00');

INSERT INTO orders
    VALUES (004, 3, 4, 6, '2026-07-27 12:00:00');

INSERT INTO orders
    VALUES (005, 3, 5, 1, '2026-07-27 17:00:00');


-- Order items table:
INSERT INTO order_items
    VALUES (1, 001, 101, 2, 'No onions');

INSERT INTO order_items
    VALUES (2, 001, 102, 1, 'Extra ketchup');

INSERT INTO order_items
    VALUES (3, 002, 103, 1, 'Extra cheese');

INSERT INTO order_items
    VALUES (4, 003, 102, 2, NULL);

INSERT INTO order_items
    VALUES (5, 004, 105, 1, 'No croutons');

INSERT INTO order_items
    VALUES (6, 005, 106, 1, NULL);


