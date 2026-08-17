SET search_path TO lyfter_car_rental;

DO $$
DECLARE
    v_email VARCHAR(50);
    v_username VARCHAR(30);

BEGIN
    SELECT username INTO v_username
    FROM users
    WHERE username = 'nalcide0';

    IF FOUND THEN
        RAISE EXCEPTION 'The username % already exists',
        v_username;
    END IF;

    SELECT email INTO v_email
    FROM users
    WHERE email = 'nalcide0@oakley.com';

    IF FOUND THEN 
        RAISE EXCEPTION 'The email % is already tied to an account',
        v_email;
    END IF;

    INSERT INTO users (id, full_name, email, username, password, date_of_birth, status)
    VALUES (51, 'Noble Alcide', 'nalcide0@oakley.com', 'nalcide0', 'xF7|TWw,D', '1954-06-04', 'payment pending');

END $$