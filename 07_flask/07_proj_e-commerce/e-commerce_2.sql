SET search_path TO e_commerce;

-- Crea el índice en PostgreSQL:
CREATE UNIQUE INDEX uq_one_default_method_per_user
ON e_commerce.user_payment_methods (user_id)
WHERE is_default = TRUE;

-- Verifica que se haya creado:
SELECT indexname, indexdef
FROM pg_indexes
WHERE schemaname = 'e_commerce'
  AND tablename = 'carts';

-- Comprueba que no haya carritos activos duplicados:
SELECT user_id, COUNT(*)
FROM e_commerce.carts
WHERE status = 'Active'
GROUP BY user_id
HAVING COUNT(*) > 1;


ALTER TABLE cart_products
ADD COLUMN total_price FLOAT NOT NULL;

DELETE FROM invoice_products
WHERE invoice_id = 6;

DELETE FROM invoices
WHERE id = 6;

ALTER TABLE invoices
ALTER COLUMN id RESTART WITH 4;

DELETE FROM e_commerce.carts
WHERE id = 4;

ALTER TABLE e_commerce.carts
ALTER COLUMN id RESTART WITH 1;

ALTER TABLE e_commerce.cart_products
ALTER COLUMN id RESTART WITH 1;

INSERT INTO e_commerce.invoice_products
VALUES (7, 6, 3, 2, 3800);

INSERT INTO e_commerce.invoice_products
VALUES (8, 6, 5, 2, 2340);

SELECT * FROM e_commerce.invoice_products;

ALTER TABLE billing_addresses
ALTER COLUMN id RESTART WITH 2;

ALTER TABLE invoices
ADD COLUMN billing_address_id INTEGER REFERENCES billing_addresses(id);

ALTER TABLE invoices
ADD COLUMN user_payment_method_id INTEGER REFERENCES user_payment_methods(id);

ALTER TABLE invoices
ADD COLUMN status VARCHAR(50) CHECK (status IN ('Completed', 'Returned'));

UPDATE invoices
SET status = 'Completed';

ALTER TABLE invoice_products
ALTER COLUMN id RESTART WITH 4;

SELECT * FROM e_commerce.invoices;

UPDATE e_commerce.invoices
SET user_payment_method_id = 2
WHERE id = 1;

UPDATE e_commerce.invoices
SET user_payment_method_id = 1
WHERE id = 2;

UPDATE e_commerce.invoices
SET user_payment_method_id = 3
WHERE id = 3;
