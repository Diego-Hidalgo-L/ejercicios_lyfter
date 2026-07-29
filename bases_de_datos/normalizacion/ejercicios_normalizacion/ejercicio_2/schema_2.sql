-- SQLite


-- OWNERS:
-- Esta tabla incluye sólo la información que depende directamente del Customer y de nada más.

CREATE TABLE owners (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(10) NOT NULL,
    phone_number CHAR(12) NOT NULL
);


-- MAKES:
-- Esta tabla incluye sólo la información que depende directamente del Make y de nada más.

CREATE TABLE makes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    make VARCHAR(10) NOT NULL
);


-- MODELS:
-- 1:N entre Make:Models - Cada Make puede tener varios Models, pero cada Model puede pertenecer únicamente a un solo Make.

CREATE TABLE models (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    make_id INTEGER REFERENCES makes(id),
    model VARCHAR(15) NOT NULL,
    year SMALLINT NOT NULL,
    color VARCHAR(10) NOT NULL
);


-- CARS:
-- 1:N entre Models:VIN - Cada Model puede estar en varios VIN, pero cada VIN puede tener únicamente un solo Model.

CREATE TABLE cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vin VARCHAR(11) NOT NULL,
    model_id INTEGER REFERENCES models(id)
);


-- CAR OWNERS:
-- Insurance company e Insurance policy dependen de la llave compuesta Car ID / Owner ID, por se mantienen dentro de la misma tabla.

CREATE TABLE car_owners (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_id INTEGER REFERENCES cars(id),
    owner_id INTEGER REFERENCES owners(id),
    insurance_company VARCHAR(20) NOT NULL,
    insurance_policy VARCHAR(20) NOT NULL
);