
1FN:
    - Ya se cumple porque no hay más de una columna para el mismo dato ni hay más de un solo dato en cada celda.

2FN:
    - Student ID + Course Code = llave compuesta.
    - Separamos la llave compuesta en las siguientes tablas:
    - Students:
        a. Student ID.
        b. Student Name.
    - Courses:
        a. Course ID.
        b. Course Code.
        c. Course Name.
        d. Instructor.
        e. Instructor Email.

3FN:
    - Se separan los datos en las siguientes tablas conforme a su dependencia a la llave primaria de la tabla anterior:
    - Students:
        a. ID.
        b. Student Name.
    - Instructors:
        a. ID.
        b. Instructor Email --> Instructor Name.
    - Courses:
        a. ID.
        b. Course Name + Course Instructor --> Course Code.
    - Student Courses:
        a. ID.
        b. Student ID + Course ID (llave compuesta).