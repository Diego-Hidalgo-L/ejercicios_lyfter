-- SQLite

-- Owners table:
INSERT INTO owners
    VALUES (1, 'Alice', '123-456-7890');

INSERT INTO owners
    VALUES (2, 'Bob', '987-654-3210');

INSERT INTO owners
    VALUES (3, 'Claire', '555-123-4567');

INSERT INTO owners
    VALUES (4, 'Dave', '111-222-3333');


-- Makes table:
INSERT INTO makes
    VALUES (1, 'Honda');

INSERT INTO makes
    VALUES (2, 'Chevrolet');


-- Moldes table:
INSERT INTO models
    VALUES (1, 1, 'Accord', 2003, 'Silver');

INSERT INTO models
    VALUES (2, 1, 'CR-V', 2014, 'Blue');

INSERT INTO models
    VALUES (3, 2, 'Volt', 2015, 'Red');


-- Cars table:
INSERT INTO cars
    VALUES (1, '1HGCM82633A', 1);

INSERT INTO cars
    VALUES (2, '5J6RM4H79EL', 2);

INSERT INTO cars
    VALUES (3, '1G1RA6EH1FU', 3);


-- Car Owners table:
INSERT INTO car_owners
    VALUES (1, 1, 1, 'ABC Insurance', 'Fire & Theft');

INSERT INTO car_owners
    VALUES (2, 1, 2, 'XYZ Insurance', 'Full Cover');

INSERT INTO car_owners
    VALUES (3, 2, 3, 'DEF Insurance', 'Collision');

INSERT INTO car_owners
    VALUES (4, 3, 4, 'GHI Insurance', 'Basic Legal');