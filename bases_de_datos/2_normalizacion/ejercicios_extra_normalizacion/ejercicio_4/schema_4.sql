-- SQLite

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name VARCHAR(20) NOT NULL
);

CREATE TABLE instructors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    instructor_name VARCHAR(20) NOT NULL,
    instructor_email VARCHAR(20) NOT NULL
);

CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code CHAR(5) NOT NULL,
    course_name VARCHAR(15) NOT NULL,
    course_instructor INTEGER REFERENCES instructors(id)
);

CREATE TABLE student_courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER REFERENCES students(id),
    course_id INTEGER REFERENCES courses(id)
);