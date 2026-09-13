SET search_path TO lyfter_car_rental;

DO $$
DECLARE
    v_user_status VARCHAR(30);
    v_car_status VARCHAR(30);
    v_car_id INTEGER;

BEGIN
    SELECT status INTO v_user_status
    FROM users
    WHERE id = 40;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'User % not found',
        40;
    END IF;

    IF v_user_status != 'active' THEN
        RAISE EXCEPTION 'User % is not active',
        40;
    END IF;

    -- Verifico si el user ya está alquilando otro carro
    SELECT car_id INTO v_car_id
    FROM rentals
    WHERE user_id = 40
        AND status = 'ongoing';

    IF FOUND THEN
        RAISE EXCEPTION 'User ID % is already renting a car (ID %)',
        40, v_car_id;
    END IF;

    SELECT status INTO v_car_status
    FROM cars
    WHERE id = 1;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Car ID % not found',
        1;
    END IF;

    IF v_car_status != 'available' THEN
        RAISE EXCEPTION 'Car ID % is not available for rent',
        1;
    END IF;

    INSERT INTO rentals (car_id, user_id, rental_date, status)
    VALUES (1, 40, '2026-08-10', 'ongoing');

    UPDATE cars
    SET status = 'rental ongoing'
    WHERE id = 1;

END $$