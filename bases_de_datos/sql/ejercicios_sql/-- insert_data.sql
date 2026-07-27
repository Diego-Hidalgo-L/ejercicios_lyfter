-- SQLite

INSERT INTO users (id, full_name, email, registration_date, cart_id)
    VALUES (1, 'John Lennon', 'j.lennon@gmail.com', '2022-05-16', 1);

INSERT INTO shopping_carts (id, user_id)
    VALUES (1, 1);

INSERT INTO users (id, full_name, email, registration_date, cart_id)
    VALUES (2, 'Jimi Hendrix', 'jimi_hendrix@hotmail.com', '2019-01-05', 2);

INSERT INTO shopping_carts (id, user_id)
    VALUES (2, 2);

INSERT INTO payment_methods (id, method_type, bank_name)
    VALUES (1, 'Cash', 'n/a');

INSERT INTO payment_methods (id, method_type, bank_name)
    VALUES (2, 'Credit/debit card', 'BAC');

INSERT INTO payment_methods (id, method_type, bank_name)
    VALUES (3, 'Promo code', 'n/a');

INSERT INTO products (id, code, name, price, entry_date, brand, stock_available)
    VALUES (1, 65488, 'iPhone', 699.99, '2026-02-01', 'Apple', 12);

INSERT INTO products (id, code, name, price, entry_date, brand, stock_available)
    VALUES (2, 15987, 'iPad', 899.99, '2025-08-12', 'Apple', 5);

INSERT INTO products (id, code, name, price, entry_date, brand, stock_available)
    VALUES (3, 48875, 'MacBook Pro', 1999.99, '2026-03-09', 'Apple', 9);

INSERT INTO shopping_cart_products (id, cart_id, product_id, quantity)
    VALUES (1, 1, 1, 2);

INSERT INTO shopping_cart_products (id, cart_id, product_id, quantity)
    VALUES (2, 2, 1, 1);

INSERT INTO shopping_cart_products (id, cart_id, product_id, quantity)
    VALUES (3, 2, 2, 1);

INSERT INTO shopping_cart_products (id, cart_id, product_id, quantity)
    VALUES (4, 1, 3, 1);

INSERT INTO invoices (id, invoice_number, purchase_date, user_id, total_amount)
    VALUES (1, 759, '2026-07-14', 1, 3399.99);

INSERT INTO invoices (id, invoice_number, purchase_date, user_id, total_amount)
    VALUES (2, 773, '2026-07-15', 2, 1599.99);

UPDATE invoices SET
    payment_method_id = 2,
    phone_number = '6767-0991',
    employee_code = 598145
    WHERE id = 1;

UPDATE invoices SET
    payment_method_id = 3,
    phone_number = '8765-3321',
    employee_code = 366658
    WHERE id = 2;

INSERT INTO invoice_products (id, invoice_id, product_id, quantity, total_amount)
    VALUES (1, 1, 1, 2, 1399.99);

INSERT INTO invoice_products (id, invoice_id, product_id, quantity, total_amount)
    VALUES (2, 1, 3, 1, 1999.99);

INSERT INTO invoice_products (id, invoice_id, product_id, quantity, total_amount)
    VALUES (3, 2, 1, 1, 699.99);

INSERT INTO invoice_products (id, invoice_id, product_id, quantity, total_amount)
    VALUES (4, 2, 2, 1, 899.99);

INSERT INTO reviews (id, user_id, product_id, comment, rating, date)
    VALUES (1, 1, 3, 'Simply awful...', 1, '2026-07-16');

INSERT INTO reviews (id, user_id, product_id, comment, rating, date)
    VALUES (2, 2, 2, 'Perfect!', 5, '2026-07-14');

INSERT INTO reviews (id, user_id, product_id, comment, rating, date)
    VALUES (3, 1, 1, 'My kids love it!', 4, '2026-07-16');

INSERT INTO invoices
    VALUES (3, 2, 785, '2026-07-15', 1, 899.99, '8765-3321', 935731);

INSERT INTO invoice_products
    VALUES (5, 3, 2, 1, 899.99);

