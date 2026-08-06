SET search_path TO ejercicio;

DO $$
DECLARE
    v_user_id INTEGER;
    v_stock INTEGER;
    v_bill_id INTEGER;
	item RECORD;

BEGIN
    -- 1. Verifico que el usuario exista en nuestra DB.
    SELECT id INTO v_user_id
    FROM users
    WHERE user_name = 'Kurt Cobain';

    IF v_user_id IS NULL THEN
        RAISE EXCEPTION 'El usuario no se encuentra en la base de datos. Abortando transacción.';
    END IF;


    -- 2. Creo una tabla temporal con todos los productos de la compra.ABORT
    CREATE TEMP TABLE purchase_items (
        product_id INTEGER,
        quantity SMALLINT
    ) ON COMMIT DROP;

    INSERT INTO purchase_items (product_id, quantity)
        VALUES
            (4, 4),
            (7, 2),
            (1, 3);


    -- 3. Verifico el stock de cada producto ANTES de registrarlos.
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

    END LOOP;


    -- 4. SOLO si TODOS los productos están en stock, creamos la factura y registramos todos los productos en bill_products.
    INSERT INTO bills (user_id, address_id, purchase_date, status, delivery_date)
        VALUES (3, 5, '2026-08-05', 'Pending', NULL)
        RETURNING id INTO v_bill_id;

    INSERT INTO bill_products (bill_id, product_id, quantity)
        VALUES
            (v_bill_id, 4, 4),
            (v_bill_id, 7, 2),
            (v_bill_id, 1, 3);

    -- 5. Una vez hecha la factura, modificamos el stock de productos.
    FOR item IN
        SELECT product_id, quantity
        FROM purchase_items
    
    LOOP
        UPDATE products
        SET stock = stock - item.quantity
        WHERE id = item.product_id;

    END LOOP;

END $$;