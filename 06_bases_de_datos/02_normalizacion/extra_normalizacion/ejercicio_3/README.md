
1FN:
    - Ya se cumple porque no hay más de una columna para el mismo dato ni hay más de un solo dato en cada celda.

2FN:
    - Employee ID + Project ID = llave compuesta.
    - Separamos la llave compuesta en las siguientes tablas:
    - Employees:
        a. Employee ID.
        b. Employee Name.
        c. Department Name.
        d. Department Phone.
    - Projects:
        a. Project ID.
        b. Project Name.
        c. Project Budget.

3FN:
    - Se separan los datos en las siguientes tablas conforme a su dependencia a la llave primaria de la tabla anterior:
    - Departments:
        a. ID.
        b. Department --> Department Name.
    - Employees:
        a. ID.
        b. Department ID --> Employee Name.
    - Projects:
        a. ID.
        b. Budget --> Project Name.
    - Project Employees:
        a. ID.
        b. Project ID + Employee ID (llave compuesta).