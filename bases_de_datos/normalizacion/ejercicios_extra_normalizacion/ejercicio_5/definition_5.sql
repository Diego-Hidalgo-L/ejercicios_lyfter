-- SQLite

-- Patients table:
INSERT INTO patients
    VALUES (1, 'Diana Vargas', '8888-1111');

INSERT INTO patients
    VALUES (2, 'Edwin Mora', '8999-2222');


-- Doctors table:
INSERT INTO doctors
    VALUES (1, 'Dr. Soto', 'Pediatría');

INSERT INTO doctors
    VALUES (2, 'Dra. Mora', 'Cardiología');


-- Appointments table:
INSERT INTO appointments
    VALUES ('A01', 1, 1, '2024-08-01 10:00:00');

INSERT INTO appointments
    VALUES ('A02', 1, 1, '2024-08-10 10:00:00');

INSERT INTO appointments
    VALUES ('A03', 2, 2, '2024-08-05 13:00:00');