SET search_path TO lyfter_car_rental;

DO $$
DECLARE
    v_car_id INTEGER;
    v_rental_status VARCHAR(30);
    v_car_status VARCHAR(30);

BEGIN
    SELECT car_id, status INTO v_car_id, v_rental_status
    FROM rentals
    WHERE id = 1;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Rental ID % not found',
        1;
    END IF;

    IF v_rental_status = 'returned' THEN
        RAISE EXCEPTION 'Rental ID % has already been returned',
        1;
    END IF;

    SELECT status INTO v_car_status
    FROM cars
    WHERE id = v_car_id;

    -- No verifico si el car_id existe, porque si el rental existe el car también debe existir.
    IF v_car_status = 'available' THEN
        RAISE EXCEPTION 'Car % is already available',
        v_car_id;
    END IF;

    UPDATE rentals
    SET status = 'returned', return_date = '2026-08-16'
    WHERE id = 1;

    UPDATE cars
    SET status = 'available'
    WHERE id = v_car_id;

END $$