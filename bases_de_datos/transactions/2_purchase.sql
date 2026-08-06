SET search_path TO ejercicio;

DO $$
DECLARE
    -- Definimos variables para almacenar datos durante la ejecución.
    v_user_id INTEGER;
    v_stock INTEGER;
    item RECORD;

BEGIN
    -- 1. Validar el usuario.
    -- Si el usuario existe en nuestra DB, obtenemos el id y lo guardamos en nuestra variable.
    SELECT id INTO v_user_id
    FROM users
    WHERE user_name = 'John Lennon';

    -- Si el usuario no existe, lanzamos un error y detenemos todo.
    IF v_user_id IS NULL THEN
        RAISE EXCEPTION 'El usuario no se encuentra en la base de datos. Abortando transacción.';
    END IF;


    -- 2. Crear la factura.
    INSERT INTO bills (user_id, address_id, purchase_date, status, delivery_date) 
        VALUES (v_user_id, 1, '2026-07-31', 'Pending', NULL);


    -- 3. Ingresar productos en bill_products para poder iterar y verificar el stock de cada uno.
    INSERT INTO bill_products (bill_id, product_id, quantity)
        VALUES
        (4, 1, 1),
        (4, 3, 1),
        (4, 8, 1);
    

    -- 4. Iterar los productos de cada bill a través de bill_products y verificar el stock de cada uno.
    FOR item IN
        SELECT product_id, quantity
        FROM bill_products
        WHERE bill_id = 1
    
	LOOP
        -- 5. Obtener el stock actual de cada producto y guardarlo en una variable.
        SELECT stock INTO v_stock
        FROM products
        WHERE id = item.product_id;
    
        -- Si el producto no existe, lanzamos un error.
        IF v_stock IS NULL THEN
            RAISE EXCEPTION 'El producto % no existe. Abortando transacción.',
            item.product_id;
        END IF;

        -- Si no hay stock suficiente, lanzamos un error y detenemos todo.
        IF v_stock < item.quantity THEN
            RAISE EXCEPTION 'Stock insuficiente para el producto %. Disponible: %, solicitado: %.',
                item.product_id,
                v_stock,
                item.quantity;
        END IF;


        -- 6. Actualizamos el stock.
        UPDATE products
        SET stock = stock - item.quantity
        WHERE id = item.product_id;

    END LOOP;

END $$;