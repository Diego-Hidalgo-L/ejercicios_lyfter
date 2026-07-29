-- SQLite

CREATE TABLE departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    department_name VARCHAR(15) NOT NULL,
    phone_number CHAR(9)
);

CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_name VARCHAR(20) NOT NULL,
    department_id INTEGER REFERENCES departments(id)
);

CREATE TABLE projects (
    id CHAR(4) PRIMARY KEY NOT NULL,
    project_name VARCHAR(15) NOT NULL,
    budget INTEGER
);

CREATE TABLE project_employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id CHAR(4) REFERENCES projects(id),
    employee_id INTEGER REFERENCES employees(id)
);