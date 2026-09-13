-- SQLite

-- 2. Agrupamiento y conteo cruzado.
    -- Usando las tablas de Books, Customers y Rents:
        -- Obtenga el número total de veces que cada cliente ha rentado un libro.
        -- Ordene de mayor a menor y limite el resultado a los 3 clientes más activos.
    -- Debe usar: GROUP BY, COUNT(), ORDER BY, LIMIT.

SELECT customers.customer_name, COUNT(rents.customer_id) AS books_rented
    FROM customers
    LEFT JOIN rents
    ON customers.id = rents.customer_id
    GROUP BY customers.customer_name
    ORDER BY books_rented DESC
    LIMIT 3;


-- 3. Consulta con múltiples JOINS anidados.
    -- Genere un SELECT que devuelva lo siguiente:
        -- Nombre del cliente.
        -- Nombre del libro.
        -- Nombre del autor.
        -- Estado del alquiler (Rents.State).
    -- Debe manejar el caso en que un libro no tenga autor.

SELECT customers.customer_name, books.book_name, authors.author_name, rents.state
    FROM rents
    INNER JOIN customers
    ON rents.customer_id = customers.id
    INNER JOIN books
    ON rents.book_id = books.id
    INNER JOIN authors
    ON books.author_id = authors.id;
