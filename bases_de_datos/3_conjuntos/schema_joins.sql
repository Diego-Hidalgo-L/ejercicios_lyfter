-- SQLite

CREATE TABLE authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_name VARCHAR(20) NOT NULL
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_name VARCHAR(20) NOT NULL,
    author_id INTEGER REFERENCES authors(id)
);

CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name VARCHAR(20) NOT NULL,
    customer_email VARCHAR(20)
);

CREATE TABLE rents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER REFERENCES books(id),
    customer_id INTEGER REFERENCES customers(id),
    state VARCHAR(15) NOT NULL
);