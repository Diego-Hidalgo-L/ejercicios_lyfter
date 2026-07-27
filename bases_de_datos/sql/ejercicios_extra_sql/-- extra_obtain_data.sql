-- SQLite

SELECT *
    FROM products;

SELECT *
    FROM products
    WHERE price > 50000;

SELECT *
    FROM products
    WHERE product_name LIKE '%apple%';

SELECT *
    FROM products
    ORDER BY price DESC LIMIT 5;

SELECT *
    FROM products
    ORDER BY id ASC LIMIT 10;