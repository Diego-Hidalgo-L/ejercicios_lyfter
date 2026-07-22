SQLite

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(25) NOT NULL,
    email VARCHAR(25) UNIQUE NOT NULL,
    registration_date DATE NOT NULL,
    cart_id INTEGER UNIQUE
);

CREATE TABLE payment_methods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    method_type VARCHAR(10) NOT NULL,
    bank_name VARCHAR(10) NOT NULL
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code CHAR(5) NOT NULL,
    name VARCHAR(15) NOT NULL,
    price FLOAT NOT NULL,
    entry_date DATE NOT NULL,
    brand VARCHAR(10) NOT NULL,
    stock_available SMALLINT NOT NULL
);

CREATE TABLE shopping_carts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE REFERENCES users(id)
);

CREATE TABLE shopping_cart_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER REFERENCES shopping_carts(id),
    product_id INTEGER REFERENCES products(id),
    quantity SMALLINT NOT NULL
);

CREATE TABLE invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES users(id),
    invoice_number SMALLINT NOT NULL,
    purchase_date DATE NOT NULL,
    payment_method_id INTEGER REFERENCES payment_methods(id),
    total_amount FLOAT NOT NULL
);

CREATE TABLE invoice_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER REFERENCES invoices(id),
    product_id INTEGER REFERENCES products(id),
    quantity SMALLINT NOT NULL,
    total_amount FLOAT NOT NULL
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES users(id),
    product_id INTEGER REFERENCES products(id),
    comment TEXT NOT NULL,
    rating SMALLINT NOT NULL,
    date DATE NOT NULL
);
