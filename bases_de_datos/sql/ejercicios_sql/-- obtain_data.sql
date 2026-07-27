-- SQLite

-- All stored products:
SELECT *
    FROM products;

-- All products above $50,000:
SELECT *
    FROM products
    WHERE price > 50000;

-- All purchases of one product by its ID:
SELECT *
    FROM invoice_products
    WHERE product_id = 1;

-- All purchases grouped by product ID, showing total quantity:
SELECT product_id, SUM(quantity)
    FROM invoice_products
    GROUP BY product_id;

-- All invoices that belong to the same specific buyer:
SELECT *
    FROM invoices
    WHERE user_id = 2;

-- All invoices ordered by total amount in descending order:
SELECT *
    FROM invoices
    ORDER BY total_amount DESC;

-- A single invoice by its invoice number:
SELECT *
    FROM invoices
    WHERE invoice_number = 773;