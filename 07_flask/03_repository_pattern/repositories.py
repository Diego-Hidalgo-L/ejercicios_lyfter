
class UsersRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_user(self, user_record):
        return {
            "id": user_record[0],
            "full_name": user_record[1],
            "email": user_record[2],
            "password": user_record[3],
        }

    def create(self, full_name, email, password):
        try:
            self.db_manager.execute_query("""
            INSERT INTO python_sql.users
            VALUES (%s, %s, %s);""",
            (full_name, email, password)
            ) # No se hace self.db_manager.commit() porque .execute_query() ya hace el commit internamente.

            print("User inserted successfully!")
            return True
        
        except Exception as error:
            print("Error inserting user into the database:", error)
            return False

    def get_all(self):
        try:
            results = self.db_manager.execute_query("""
                SELECT id, full_name, email, password
                FROM python_sql.users;"""
                )
            formatted_results = [self._format_user(result) for result in results]

            return formatted_results

        except Exception as error:
            print("Error getting all users from database:", error)
            return False

    def get_by_id(self, _id):
        try:
            result = self.db_manager.execute_query("""
                SELECT *
                FROM python_sql.users
                WHERE id = %s;""",
                (_id,) # Esta coma convierte el parámetro en una TUPLA DE UN ELEMENTO.
                ) 
            formatted_result = self._format_user(result[0])

            return formatted_result

        except Exception as error:
            print(f"Error getting user '{_id}' from the database:", error)
            return False

    def update(self, full_name, email, password, _id): # (PUT): Implementar validación de que el usuario existe. 
        try:
            self.db_manager.execute_query("""
                UPDATE python_sql.users
                SET (full_name, email, password) = (%s, %s, %s)
                WHERE id = _id;""",
                (full_name, email, password, _id), # Trailing commas no son un problema en Python (En PL/pgSQL sí)
            )

            print(f"User '{_id}' updated successfully")
            return True

        except Exception as error:
            print(f"Error updating user '{_id}'", error)
            return False

# Implementar otro método que funcione como un PATCH.

    def delete(self, _id):
        try:
            self.db_manager.execute_query("""
                DELETE FROM python_sql.users
                WHERE id = %s;""", # ¡ATENCIÓN! Si no pongo WHERE eliminaría todos los usuarios.
                (_id,)
            )

            print(f"User {_id} deleted successfully")
            return True
        
        except Exception as error:
            print(f"Error deleting user {_id}:", error)
            return False

