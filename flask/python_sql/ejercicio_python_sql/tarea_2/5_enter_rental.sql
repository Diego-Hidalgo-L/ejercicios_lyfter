SET search_path TO lyfter_car_rental;

DO $$
DECLARE
    v_user_status VARCHAR(30);
    v_car_status VARCHAR(30);

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

    INSERT INTO rentals (id, car_id, user_id, rental_date, status)
    VALUES (1, 1, 40, '2026-08-16', 'ongoing');

END $$