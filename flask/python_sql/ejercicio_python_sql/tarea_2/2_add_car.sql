SET search_path TO lyfter_car_rental;

-- No valido el license_plate porque ya tiene constraint de UNIQUE en la tabla.

INSERT INTO cars (id, license_plate, brand, model, year, status)
VALUES (21, 'CWQ653', 'Mazda', 'Millenia', 2001, 'available');