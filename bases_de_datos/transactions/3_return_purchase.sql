SET search_path TO ejercicio;

DO $$
DECLARE
    -- 1. Definimos variables para almacenar datos durante la ejecución.
    v_bill_id INTEGER;
    v_status VARCHAR(15);
    item RECORD;

BEGIN
    -- 2. Verificar si la factura existe en la DB.
    SELECT id, status
    INTO v_bill_id, v_status
    FROM bills
    WHERE id = 2;

    -- Si la factura no existe, lanzamos un error.
    IF v_bill_id IS NULL THEN
        RAISE EXCEPTION 'La factura % no existe. Abortando transacción.',
        2;
    END IF;

    -- Si la factura ya fue retornada previamente, lanzamos un error.
    IF v_status = 'Returned' THEN
        RAISE EXCEPTION 'La factura % ya fue retornada.',
        2;
    END IF;

    -- Si la factura ya fue cancelada anteriormente, lanzamos un error.ABORT
    IF v_status = 'Cancelled' THEN
        RAISE EXCEPTION 'La factura % ya fue cancelada.',
        2;
    END IF;

    -- 3. Recorrer todos los productos de la factura.
    FOR item IN
        SELECT product_id, quantity
        FROM bill_products
        WHERE bill_id = v_bill_id
    LOOP

        -- 4. Aumentar el stock de los productos en la cantidad que se registró en la compra.
        UPDATE products
        SET stock = stock + item.quantity
        WHERE id = item.product_id;
    
    END LOOP;

    -- 5. Modificar la factura original para marcarla con el estado de "Retornada".
    UPDATE bills
    SET status = 'Returned'
    WHERE id = v_bill_id;

END $$;