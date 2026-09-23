SET search_path TO authentication;

DROP TABLE invoice_products;
DROP TABLE invoices;
DROP TABLE products;
DROP TABLE users;

SELECT * FROM authentication.users
ORDER BY id ASC;

DELETE FROM authentication.invoice_products;
DELETE FROM authentication.invoices;

DELETE FROM authentication.users
WHERE id = 9;

ALTER TABLE authentication.users
ALTER COLUMN id RESTART WITH 7;

ALTER TABLE authentication.invoice_products
ALTER COLUMN id RESTART WITH 1;