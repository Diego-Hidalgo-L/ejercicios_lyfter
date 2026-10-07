SET search_path TO e_commerce;

ALTER TABLE users
ALTER COLUMN id RESTART WITH 1;

SELECT * FROM users;

DROP TABLE invoice_products;
DROP TABLE invoices;
DROP TABLE products;
DROP TABLE users;