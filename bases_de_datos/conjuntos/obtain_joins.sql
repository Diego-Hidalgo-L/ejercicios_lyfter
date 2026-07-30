-- SQLite

-- 1) Obtenga todos los libros y sus autores (en caso de tenerlos):
SELECT books.book_name, authors.author_name
    FROM books
    LEFT JOIN authors
    ON books.author_id = authors.id;

-- 2) Obtenga todos los libros que NO tienen autor:
SELECT books.book_name, authors.author_name
    FROM books
    LEFT JOIN authors
    ON books.author_id = authors.id
    WHERE author_name IS NULL;

-- 3) Obtenga todos los autores que no tienen libros:
SELECT books.book_name, authors.author_name
    FROM books
    RIGHT JOIN authors
    ON books.author_id = authors.id
    WHERE book_name IS NULL;

-- 4) Obtenga todos los libros que han sido rentados en algún momento:
SELECT books.book_name, rents.customer_id, rents.state
    FROM books
    INNER JOIN rents
    ON rents.book_id = books.id;

-- 5) Obtenga todos los libros que nunca han sido rentados:
SELECT books.book_name, rents.customer_id, rents.state
    FROM books
    LEFT JOIN rents
    ON rents.book_id = books.id
    WHERE customer_id IS NULL;

-- 6) Obtenga todos los clientes que nunca han rentado un libro:
SELECT customers.customer_name, customers.customer_email, rents.book_id
    FROM customers
    LEFT JOIN rents
    ON rents.customer_id = customers.id
    WHERE book_id IS NULL;

-- 7) Obtenga todos los libros que han sido rentados y están en estado “Overdue”:
SELECT books.book_name, rents.customer_id, rents.state
    FROM books
    INNER JOIN rents
    ON books.id = rents.book_id
    WHERE state IS 'Overdue';