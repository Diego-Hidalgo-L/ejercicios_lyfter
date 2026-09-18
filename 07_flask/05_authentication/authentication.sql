SET search_path TO authentication;

DROP TABLE invoice_products;
DROP TABLE invoices;
DROP TABLE products;
DROP TABLE users;

SELECT * FROM authentication.users;

DELETE FROM authentication.invoice_products;
DELETE FROM authentication.invoices;

ALTER TABLE authentication.invoices
ALTER COLUMN id RESTART WITH 1;

ALTER TABLE authentication.invoice_products
ALTER COLUMN id RESTART WITH 1;