SET search_path TO lyfter_car_rental;

DO $$
DECLARE
    v_license_plate CHAR(6);

BEGIN
    SELECT license_plate INTO v_license_plate
    FROM cars
    WHERE license_plate = 'CWQ653';

    IF FOUND THEN
        RAISE EXCEPTION 'Car % already exists',
        'CWQ653';
    END IF;

    INSERT INTO cars (id, license_plate, brand, model, year, status)
    VALUES (21, 'CWQ653', 'Mazda', 'Millenia', 2001, 'available');

END $$