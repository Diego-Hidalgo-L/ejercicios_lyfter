-- SQLite

-- Students table:
INSERT INTO students
    VALUES (301, 'Marco Gómez');

INSERT INTO students
    VALUES (302, 'Carla Ruiz');


-- Instructors table:
INSERT INTO instructors
    VALUES (1, 'Juan Pérez', 'juan@uni.edu');

INSERT INTO instructors
    VALUES (2, 'Laura Rojas', 'laura@uni.edu');


-- Courses table:
INSERT INTO courses
    VALUES (1, 'CS101', 'Python I', 1);

INSERT INTO courses
    VALUES (2, 'CS102', 'Python II', 2);


-- Student Courses table:
INSERT INTO student_courses
    VALUES (1, 301, 1);

INSERT INTO student_courses
    VALUES (2, 301, 2);

INSERT INTO student_courses
    VALUES (3, 302, 1);