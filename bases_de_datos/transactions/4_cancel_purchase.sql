SET search_path TO ejercicio;

DO $$
DECLARE
    v_bill_id INTEGER;
    v_status VARCHAR(15);
    item RECORD;

BEGIN
    SELECT id, status INTO v_bill_id, v_status
    FROM bills
    WHERE id = 4;

    IF v_bill_id IS NULL THEN
        RAISE EXCEPTION 'La factura % no existe.',
        4;
    END IF;

    IF v_status != 'Pending' THEN
        RAISE EXCEPTION 'La factura % no puede ser cancelada porque su estado actual es "%".',
        v_bill_id,
        v_status;
    END IF;

    UPDATE bills
    SET status = 'Cancelled'
    WHERE id = v_bill_id;

    FOR item IN
        SELECT product_id, quantity
        FROM bill_products
        WHERE bill_id = v_bill_id
    
    LOOP
        UPDATE products
        SET stock = stock + item.quantity
        WHERE id = item.product_id;
    
    END LOOP;

END $$;