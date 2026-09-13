SET search_path TO ejercicio;

DO $$
DECLARE
    v_user_id INTEGER;
    v_bill_id INTEGER;
    v_stock SMALLINT;
    v_rows_updated INTEGER;
    item RECORD;

BEGIN
    SELECT id INTO v_user_id
    FROM users
    WHERE user_name = 'Jimi Hendrix';

    IF v_user_id IS NULL THEN
        RAISE EXCEPTION 'El usuario no existe.';
    END IF;

    -- 1. Crear tabla temporal.
    CREATE TEMP TABLE purchase_items (
        product_id INTEGER,
        quantity SMALLINT,
        original_stock SMALLINT
    ) ON COMMIT DROP;

    INSERT INTO purchase_items (product_id, quantity)
        VALUES (9, 1);

    -- 2. Verificar el stock del producto AL INICIO de la transacción
    FOR item IN
        SELECT product_id, quantity
        FROM purchase_items
    
    LOOP
        SELECT stock INTO v_stock
        FROM products
        WHERE id = item.product_id;

        IF v_stock IS NULL THEN
            RAISE EXCEPTION 'El producto % no existe. Abortando transacción.',
            item.product_id;
        END IF;

        IF v_stock < item.quantity THEN
            RAISE EXCEPTION 'Stock insuficiente para el producto %. Disponible: %, solicitado: %.',
                    item.product_id,
                    v_stock,
                    item.quantity;
        END IF;

        -- Si todo está bien con el stock del producto, registramos su stock original en nuestra tabla temporal.
        UPDATE purchase_items
        SET original_stock = v_stock
        WHERE product_id = item.product_id;
    
    END LOOP;

    -- 3. Creamos la factura y la registramos en bill_products.
    INSERT INTO bills (user_id, address_id, purchase_date, status, delivery_date)
        VALUES (v_user_id, 3, CURRENT_DATE, 'Pending', NULL)
        RETURNING id INTO v_bill_id;
    
    INSERT INTO bill_products (bill_id, product_id, quantity)
        SELECT v_bill_id, product_id, quantity
        FROM purchase_items;
    
    -- 4. Volvemos a verificar el stock del producto y si este sigue siendo stock = v_stock procedemos a reducir el stock
    FOR item IN
        SELECT product_id, quantity, original_stock
        FROM purchase_items
    
    LOOP
        UPDATE products
        SET stock = stock - item.quantity
        WHERE id = item.product_id
            AND stock = item.original_stock;

        GET DIAGNOSTICS v_rows_updated = ROW_COUNT;

        IF v_rows_updated = 0 THEN
            RAISE EXCEPTION '¡Atención! El stock del producto % cambió externamente durante la transacción. Compra abortada.',
            item.product_id;
        END IF;
    
    END LOOP;

END $$;