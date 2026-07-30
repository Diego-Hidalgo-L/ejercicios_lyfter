-- SQLite

-- Authors:
INSERT INTO authors
    VALUES (1, 'Miguel de Cervantes');

INSERT INTO authors
    VALUES (2, 'Dante Alighieri');

INSERT INTO authors
    VALUES (3, 'Takehiko Inoue');

INSERT INTO authors
    VALUES (4, 'Akira Toriyama');

INSERT INTO authors
    VALUES (5, 'Walt Disney');


-- Books:
INSERT INTO books
    VALUES (1, 'Don Quijote', 1);

INSERT INTO books
    VALUES (2, 'La Divina Comedia', 2);

INSERT INTO books
    VALUES (3, 'Vagabond 1-3', 3);

INSERT INTO books
    VALUES (4, 'Dragon Ball 1', 4);

INSERT INTO books
    VALUES (5, 'The Book of 5 Rings', NULL);


-- Customers:
INSERT INTO customers
    VALUES (1, 'John Doe', 'j.doe@email.com');

INSERT INTO customers
    VALUES (2, 'Jane Doe', 'jane@doe.com');

INSERT INTO customers
    VALUES (3, 'Luke Skywalker', 'darth.son@email.com');


-- Rents:
INSERT INTO rents
    VALUES (1, 1, 1, 'Returned');

INSERT INTO rents
    VALUES (2, 2, 2, 'Returned');

INSERT INTO rents
    VALUES (3, 1, 1, 'On time');

INSERT INTO rents
    VALUES (4, 3, 1, 'On time');

INSERT INTO rents
    VALUES (5, 2, 2, 'Overdue');