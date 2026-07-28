-- SQLite


-- CUSTOMERS:
-- Esta tabla incluye sólo la información que depende directamente del Customer y de nada más.

CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(10) NOT NULL,
    phone_number CHAR(12) NOT NULL
);


-- ADDRESSES:
-- 1:N - Cada Customer pueden tener varios Addresses, pero cada Address puede pertenecer a un solo Customer.

CREATE TABLE addresses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    address VARCHAR(20) NOT NULL,
    customer_id INTEGER REFERENCES customers(id)
);


-- ITEMS:
-- Esta tabla incluye únicamente información que depende del Item.
-- Me salto 104 porque así viene en el ejercicio.

CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(15) NOT NULL,
    price FLOAT NOT NULL
);


-- ORDERS:
-- 1:N - Cada Customer puede tener varias Orders, pero cada Order puede pertenecer a un único Customer.
-- Agregué un Order ID extra porque, en el ejercicio, el Order ID 002 aparece dos veces correspondientes al mismo Customer (Bob) pero cada una va para diferentes direcciones.
-- ¿Será necesario hacer una tabla extra de Delivery Time?

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER REFERENCES customers(id),
    address_id INTEGER REFERENCES addresses(id),
    total_amount FLOAT NOT NULL,
    delivery_time DATETIME NOT NULL
);


-- ORDER ITEMS:
-- N:N entre Orders:Items - Cada Order puede tener varios Items, y cada Item puede aparecer en varios Orders.

CREATE TABLE order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER REFERENCES orders(id),
    item_id INTEGER REFERENCES items(id),
    quantity SMALLINT NOT NULL,
    special_request VARCHAR(30)
);