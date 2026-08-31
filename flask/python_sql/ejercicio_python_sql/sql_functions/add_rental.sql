SET search_path TO lyfter_car_rental;

CREATE FUNCTION add_rental(
    p_user_id INTEGER,
    p_car_id INTEGER,
    p_rental_date DATE,
    p_status VARCHAR(30) DEFAULT 'ongoing',
    p_return_date DATE DEFAULT NULL
    )
RETURNS void
LANGUAGE plpgsql

AS $$
DECLARE
    v_user_status VARCHAR(30);
    v_car_status VARCHAR(30);
    v_car_id INTEGER;

BEGIN
    SELECT status INTO v_user_status
    FROM users
    WHERE id = p_user_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'User % not found',
        p_user_id;
    END IF;

    IF v_user_status != 'active' THEN
        RAISE EXCEPTION 'User % is not active',
        p_user_id;
    END IF;

    -- Verifico si el user ya está alquilando otro carro
    SELECT car_id INTO v_car_id
    FROM rentals
    WHERE user_id = p_user_id
        AND status = 'ongoing';

    IF FOUND THEN
        RAISE EXCEPTION 'User ID % is already renting a car (ID %)',
        p_user_id, v_car_id;
    END IF;

    SELECT status INTO v_car_status
    FROM cars
    WHERE id = p_car_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Car ID % not found',
        p_car_id;
    END IF;

    IF v_car_status != 'available' THEN
        RAISE EXCEPTION 'Car ID % is not available for rent',
        p_car_id;
    END IF;

    INSERT INTO rentals (car_id, user_id, rental_date, status, return_date)
    VALUES (p_car_id, p_user_id, p_rental_date, p_status, p_return_date);

    UPDATE cars
    SET status = 'rental ongoing'
    WHERE id = p_car_id;

END;
$$;
