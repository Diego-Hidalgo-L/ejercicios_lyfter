-- -- SQLite

-- CREATE TABLE patients (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     patient_name VARCHAR(20) NOT NULL,
--     patient_phone CHAR(9)
-- );

-- CREATE TABLE doctors (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     doctor_name VARCHAR(15) NOT NULL,
--     specialty VARCHAR(15) NOT NULL
-- );

CREATE TABLE appointments (
    id CHAR(3) PRIMARY KEY NOT NULL,
    patient_id INTEGER REFERENCES patients(id),
    doctor_id INTEGER REFERENCES doctors(id),
    datetime DATETIME NOT NULL
);

