SET search_path TO lyfter_car_rental;

-- No valido email ni username porque ya tienen constraints de UNIQUE en la tabla.

INSERT INTO users (id, full_name, email, username, password, date_of_birth, status)
VALUES (51, 'Noble Alcide', 'nalcide0@oakley.com', 'nalcide0', 'xF7|TWw,D', '1954-06-04', 'payment pending');