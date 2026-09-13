-- SQLite

-- Departments table:
INSERT INTO departments
    VALUES (1, 'IT', '2222-2222');

INSERT INTO departments
    VALUES (2, 'Marketing', '1111-1111');


-- Employees table:
INSERT INTO employees
    VALUES (201, 'Ana Rivera', 1);

INSERT INTO employees
    VALUES (202, 'Luis Méndez', 2);


-- Projects table:
INSERT INTO projects
    VALUES ('P001', 'Web App', 50000);

INSERT INTO projects
    VALUES ('P002', 'API REST', 25000);

INSERT INTO projects
    VALUES ('P003', 'Campaña TV', 30000);


-- Project employees:
INSERT INTO project_employees
    VALUES (1, 'P001', 201);

INSERT INTO project_employees
    VALUES (2, 'P002', 201);

INSERT INTO project_employees
    VALUES (3, 'P003', 202);