SET search_path TO e_commerce;

DELETE FROM invoice_products;
DELETE FROM invoices;

ALTER TABLE invoices
ALTER COLUMN id RESTART WITH 1;

ALTER TABLE e_commerce.user_payment_methods
ALTER COLUMN id RESTART WITH 3;

SELECT * FROM e_commerce.billing_addresses;

DROP TABLE invoice_products;
DROP TABLE invoices;
DROP TABLE products;
DROP TABLE users;