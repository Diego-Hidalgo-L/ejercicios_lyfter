
LIMITANTES:

1. Solo se puede usar AUTOINCREMENT con los tipos de dato INT o INTEGER, no con BIGINT o SMALLINT, por ejemplo.

2. El motor no acepta que escriba “FOREIGN KEY”, solamente “REFERENCES”.

3. El motor no permite usar ALTER TABLE DROP COLUMN <nombre de columna>. La única forma de eliminar o modificar columnas en SQLite es eliminando la tabla por completo y volver a escribirla con las modificaciones deseadas.
