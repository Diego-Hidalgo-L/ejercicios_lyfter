SET search_path TO ejercicio;

-- SCHEMA:
CREATE TABLE users (
	id INTEGER PRIMARY KEY,
	user_name VARCHAR(20) NOT NULL,
	email VARCHAR(30)
);

CREATE TABLE addresses (
	id INTEGER PRIMARY KEY,
	address VARCHAR(30) NOT NULL,
	user_id INTEGER REFERENCES users(id)
);

CREATE TABLE products (
	id INTEGER PRIMARY KEY,
	product_name VARCHAR(30) NOT NULL,
	price FLOAT NOT NULL,
	brand VARCHAR(30) NOT NULL,
	stock SMALLINT
);

CREATE TABLE bills (
	id INTEGER PRIMARY KEY,
	user_id INTEGER REFERENCES users(id),
	address_id INTEGER REFERENCES addresses(id),
	purchase_date DATE NOT NULL,
	status VARCHAR(15) NOT NULL, 
	delivery_date DATE
);

CREATE TABLE bill_products (
	id INTEGER PRIMARY KEY,
	bill_id INTEGER REFERENCES bills(id),
	product_id INTEGER REFERENCES products(id),
	quantity SMALLINT NOT NULL
);

-- DATA DEFINITION:

-- users table:
INSERT INTO users (id, user_name, email)
    VALUES (1, 'John Lennon', 'j.lennon@gmail.com');

INSERT INTO users (id, user_name, email)
    VALUES (2, 'Jimi Hendrix', 'jimi_hendrix@hotmail.com');

INSERT INTO users (id, user_name, email)
	VALUES (3, 'Kurt Cobain', 'kurt.cobain.1967@gmail.com');

-- addresses table:
INSERT INTO addresses (id, address, user_id)
	VALUES (1, '123 Main St', 1);

INSERT INTO addresses (id, address, user_id)
	VALUES (2, '456 Elm St', 2);

INSERT INTO addresses (id, address, user_id)
	VALUES (3, '4th Avenue', 2);

INSERT INTO addresses (id, address, user_id)
	VALUES (4, '789 Oak St', 3);

INSERT INTO addresses (id, address, user_id)
	VALUES (5, '464 Georgia St', 3);

-- products table:
SET search_path TO ejercicio;

INSERT INTO products (id, product_name, price, brand, stock)
    VALUES (1, 'iPhone', 699.99, 'Apple', 12);

INSERT INTO products (id, product_name, price, brand, stock)
    VALUES (2, 'iPad', 899.99, 'Apple', 5);

INSERT INTO products (id, product_name, price, brand, stock)
    VALUES (3, 'MacBook Pro', 1999.99, 'Apple', 9);

INSERT INTO products (id, product_name, price, brand, stock)
    VALUES (4, 'MacBook Air', 1299.99, 'Apple', 2);

INSERT INTO products (id, product_name, price, brand, stock)
    VALUES (5, 'Stanmore IV Black', 429.99, 'Marshall', 10);

INSERT INTO products (id, product_name, price, brand, stock)
    VALUES (6, 'Stanmore IV Cream', 429.99, 'Marshall', 17);

INSERT INTO products (id, product_name, price, brand, stock)
    VALUES (7, 'Woburn III Black', 599.99, 'Marshall', 5);

INSERT INTO products (id, product_name, price, brand, stock)
    VALUES (8, 'Woburn III Brown', 599.99, 'Marshall', 7);

-- bills table:
INSERT INTO bills (id, user_id, address_id, purchase_date, status, delivery_date)
	VALUES (2, 2, 3, '2026-07-29', 'Delivered', '2026-08-03');

INSERT INTO bills (id, user_id, address_id, purchase_date, status, delivery_date)
	VALUES (3, 2, 2, '2026-07-30', 'Delivered', '2026-08-03');

INSERT INTO bills (id, user_id, address_id, purchase_date, status, delivery_date)
	VALUES (4, 3, 5, '2026-08-02', 'In transit', NULL);

-- bill_products table:
INSERT INTO bill_products (id, bill_id, product_id, quantity)
	VALUES (4, 2, 4, 1);

INSERT INTO bill_products (id, bill_id, product_id, quantity)
	VALUES (5, 3, 6, 2);

INSERT INTO bill_products (id, bill_id, product_id, quantity)
	VALUES (6, 4, 5, 1);
