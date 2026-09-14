from flask import jsonify
from db import db_context
from sqlalchemy import select, insert, update, delete

# Se encarga de los queries de las tablas de nuestra base de datos.
class UsersRepository:
    def __init__(self, engine):
        self.engine = engine

    def get_user(self, username):
        stmt = select(db_context.users).where(db_context.users.c.username == username)

        with self.engine.connect() as conn:
            try:
                result = conn.execute(stmt)
                users = result.all()

                if len(users) == 0:
                    return None
                else:
                    return users[0]

            except Exception as error:
                print(error)

    def get_user_by_id(self, user_id):
        stmt = select(db_context.users).where(db_context.users.c.id == user_id)

        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            user = result.all()

            if len(user) == 0:
                return None
            else:
                return user[0]

    def insert(self, username, password, role):
        stmt = insert(db_context.users).returning(db_context.users.c.id).values(username=username, password=password, role=role)
        
        with self.engine.connect() as conn:
            try:
                result = conn.execute(stmt)
                conn.commit()
                print(f"User inserted successfully")

                return result.all()[0]

            except Exception as error:
                conn.rollback()
                return jsonify(error_message=f"Error adding user to database: {error}"), 400

    def update(self, user_id, data):
        stmt = update(db_context.users).where(db_context.users.c.id==user_id).values(name=data)

        with self.engine.connect() as conn:
            try:
                conn.execute(stmt)
                conn.commit()
                print(f"User ID {user_id} updated successfully")

            except Exception as error:
                conn.rollback()
                return jsonify(error_message=f"Error updating user ID {user_id}: {error}"), 400

    def delete(self, user_id):
        stmt = delete(db_context.users).where(db_context.users.c.id==user_id)

        with self.engine.connect() as conn:
            try:
                conn.execute(stmt)
                conn.commit()
                print(f"User ID {user_id} deleted successfully")

            except Exception as error:
                conn.rollback()
                return jsonify(error_message=f"Error deleting user ID {user_id}: {error}")


class FruitsRepository:
    def __init__(self, engine):
        self.engine = engine

    