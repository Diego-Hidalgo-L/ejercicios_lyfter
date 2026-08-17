SET search_path TO lyfter_car_rental;

DO $$
DECLARE
    v_id INTEGER;
    v_status VARCHAR(30);

BEGIN
    SELECT status INTO v_status
    FROM users
    WHERE id = 6;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'User id % does not exist',
        6;
    END IF;

    IF v_status = 'payment pending' THEN
        RAISE EXCEPTION 'The user status is already -Payment pending-';
    END IF;

    UPDATE users
    SET status = 'payment pending'
    WHERE id = 6;

END $$  