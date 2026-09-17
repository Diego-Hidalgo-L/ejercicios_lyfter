-- SQLite

UPDATE products SET
    stock_available = 0
    WHERE price <= 0;

UPDATE products SET
    price += 100
    WHERE stock_available < 10;

UPDATE products SET
    stock_available -= 1
    WHERE id = 7;