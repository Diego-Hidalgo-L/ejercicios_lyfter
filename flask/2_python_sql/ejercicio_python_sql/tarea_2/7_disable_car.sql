SET search_path TO lyfter_car_rental;

DO $$
DECLARE
	v_status VARCHAR(30);

BEGIN
    SELECT status INTO v_status
    FROM cars
    WHERE license_plate = 'QOP732';

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Car % not found',
        'QOP732';
    END IF;

    IF v_status = 'rental ongoing' THEN
        RAISE EXCEPTION 'Car % is currently on rental',
        'QOP732';
    END IF;

    IF v_status = 'rent ineligible' THEN
        RAISE EXCEPTION 'Car % is already ineligible for rent',
        'QOP732';
    END IF;

    UPDATE cars
    SET status = 'rent ineligible'
    WHERE license_plate = 'QOP732';

END $$