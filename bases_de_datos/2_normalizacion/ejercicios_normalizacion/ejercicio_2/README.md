
1FN:
    - Ya se cumple porque no hay más de una columna para el mismo dato ni hay más de un solo dato en cada celda.

2FN:
    - VIN + Owner ID = llave compuesta.
    - Separamos la llave compuesta en las siguientes tablas:
    - Cars:
        a. ID.
        b. VIN.
        c. Make.
        d. Model.
        e. Year.
        f. Color.
    - Owners:
        a. ID.
        b. Owner Name.
        c. Owner Phone.
        d. Insurance Company.
        e. Insurance Policy.

3FN:
    - Se separan los datos en las siguientes tablas conforme a su dependencia a la llave primaria de la tabla anterior:
    - Owners:
        a. ID.
        b. Owner Phone --> Owner Name.
    - Makes:
        a. ID.
        b. Make.
    - Models:
        a. ID.
        b. Model + Year --> Make ID.
    - Cars:
        a. ID.
        b. Color + Model ID --> VIN.
    - Insurance:
        a. ID.
        b. Insurance Company + Insurance Policy --> Car ID + Car Owner (llave compuesta).
