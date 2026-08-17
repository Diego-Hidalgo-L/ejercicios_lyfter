SET search_path TO lyfter_car_rental;

DO $$
DECLARE
    v_id INTEGER;
    v_status VARCHAR(30);

BEGIN
    SELECT status INTO v_status
    FROM cars
    WHERE license_plate = 'QOP732';

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Car % does not exist',
        'QOP732';
    END IF;

    IF v_status = 'rental ongoing' THEN
        RAISE EXCEPTION 'The user status is already -Payment pending-';
    END IF;

    UPDATE cars
    SET status = 'rental ongoing'
    WHERE license_plate = 'QOP732';

END $$  