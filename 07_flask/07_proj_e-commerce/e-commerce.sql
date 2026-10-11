SET search_path TO e_commerce;

DELETE FROM invoice_products;
DELETE FROM invoices;

ALTER TABLE invoices
ALTER COLUMN id RESTART WITH 1;

ALTER TABLE invoice_products
ALTER COLUMN id RESTART WITH 1;

SELECT * FROM e_commerce.invoice_products;

DROP TABLE invoice_products;
DROP TABLE invoices;
DROP TABLE products;
DROP TABLE users;