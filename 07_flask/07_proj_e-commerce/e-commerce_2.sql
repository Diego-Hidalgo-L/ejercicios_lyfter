SET search_path TO e_commerce;

DELETE FROM invoice_products
WHERE invoice_id = 6;

DELETE FROM invoices
WHERE id = 6;

ALTER TABLE invoices
ALTER COLUMN id RESTART WITH 4;

SELECT * FROM e_commerce.invoices;

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
