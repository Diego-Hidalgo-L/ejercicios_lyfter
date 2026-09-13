
1FN:
    - Ya se cumple porque no hay más de una columna para el mismo dato ni hay más de un solo dato en cada celda.

2FN:
    - Order ID + Item ID forman una llave compuesta.
    - Separamos la llave compuesta en las siguientes tablas:
    - Orders:
        a. ID.
        b. Customer Name.
        c. Address.
        d. Delivery Time.
    - Order Items:
        a. ID.
        b. Item Name.
        c. Price.
        d. Quantity.
        e. Special Request.

3FN:
    - Se separan los datos en las siguientes tablas conforme a su dependencia a la llave primaria de la tabla anterior:
    - Customers:
        a. ID.
        b. Phone Number (depende de) --> Customer Name.
    - Addresses:
        a. ID.
        b. Customer ID --> Address.
    - Items:
        a. ID.
        b. Price --> Item Name.
    - Orders:
        a. ID.
        b. Delivery Time --> Customer ID + Address ID (llave compuesta).
    - Order Items:
        a. ID.
        b. Quantity + Special Request --> Order ID + Item ID (llave compuesta).
