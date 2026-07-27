-- SQLite

ALTER TABLE invoices 
    ADD COLUMN phone_number TEXT DEFAULT 'none';

ALTER TABLE invoices 
    ADD COLUMN employee_code CHAR(6) DEFAULT '000000';
