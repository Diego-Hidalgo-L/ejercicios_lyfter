from flask import jsonify
from db import db_context
from sqlalchemy import select, insert, update, delete

# Se encarga de los queries de las tablas de nuestra base de datos.

class UsersRepository:
    def __init__(self, engine):
        self.engine = engine

    def get_user_by_username(self, username):
        with self.engine.connect() as conn:
            try:
                stmt = select(db_context.users).where(db_context.users.c.username == username)
                result = conn.execute(stmt)

                users = result.all()

                if len(users) == 0:
                    return None
                else:
                    return users[0]

            except Exception as error:
                print(f"Error getting user by username: {error}")
                return None

    def get_user_by_id(self, user_id):
        with self.engine.connect() as conn:
            try:
                stmt = select(db_context.users).where(db_context.users.c.id == user_id)
                result = conn.execute(stmt)

                user = result.all()

                if len(user) == 0:
                    return None
                else:
                    return user[0]

            except Exception as error:
                print(f"Error getting user ID {user_id}: {error}")
                return None

    def insert(self, username, password, role):
        with self.engine.connect() as conn:
            try:
                stmt = insert(db_context.users).returning(db_context.users.c.id).values(username=username, password=password, role=role)
                result = conn.execute(stmt)
                
                if len(result) == 0:
                    return None
                
                conn.commit()
                print("User inserted successfully")

                return result.all()[0]

            except Exception as error:
                conn.rollback()
                print("Error adding user to database:", error)
                return None

    def update(self, user_id, username=None, password=None, role=None):   
        with self.engine.connect() as conn:
            try:
                if username is not None:
                    stmt = update(db_context.users).where(db_context.users.c.id==user_id).values(username=username)

                if password is not None:
                    stmt = update(db_context.users).where(db_context.users.c.id==user_id).values(password=password)

                if role is not None:
                    stmt = update(db_context.users).where(db_context.users.c.id==user_id).values(role=role) # SOLO ADMINISTRATOR

                conn.execute(stmt)
                conn.commit()
                print(f"User ID {user_id} updated successfully")

            except Exception as error:
                conn.rollback()
                print(f"Error updating user ID {user_id}: {error}")
                return None

    def delete(self, user_id):
        with self.engine.connect() as conn:
            try:
                stmt = delete(db_context.users).where(db_context.users.c.id==user_id)
                conn.execute(stmt)

                conn.commit()
                print(f"User ID {user_id} deleted successfully")

            except Exception as error:
                conn.rollback()
                print(f"Error deleting user ID {user_id}: {error}")
                return None


class FruitsRepository:
    def __init__(self, engine):
        self.engine = engine

    def get_product_by_id(self, product_id):
        with self.engine.connect() as conn:
            try:
                stmt = select(db_context.products).where(db_context.products.c.id == product_id)
                result = conn.execute(stmt)

                product = result.all()

                if len(product) == 0:
                    return None
                else:
                    return product[0]

            except Exception as error:
                print(f"Error getting product ID {product_id}: {error}")
                return None

    def insert(self, name, price, entry_date, stock):
        with self.engine.connect() as conn:
            try:
                stmt = insert(db_context.products).returning(db_context.products.c.id).values(name=name, price=price, entry_date=entry_date, stock=stock)

                result = conn.execute(stmt)
                conn.commit()
                print("Product inserted successfully")

                return result.all()[0]

            except Exception as error:
                conn.rollback()
                return jsonify(error_message=f"Error adding product to database: {error}"), 400

    def update(self, product_id, name=None, price=None, entry_date=None, stock=None):
        with self.engine.connect() as conn:
            try:
                if name is not None:
                    stmt = update(db_context.products).where(db_context.users.c.id==product_id).values(name=name)

                if price is not None:
                    stmt = update(db_context.products).where(db_context.users.c.id==product_id).values(price=price)

                if entry_date is not None:
                    stmt = update(db_context.products).where(db_context.users.c.id==product_id).values(entry_date=entry_date)

                if stock is not None:
                    stmt = update(db_context.products).where(db_context.users.c.id==product_id).values(stock=stock)

                conn.execute(stmt)
                conn.commit()
                return jsonify(message=f"Product ID {product_id} updated successfully")

            except Exception as error:
                conn.rollback()
                return jsonify(error_message=f"Error updating product ID {product_id}: {error}"), 400

    def delete(self, product_id):
        stmt = delete(db_context.products).where(db_context.products.c.id==product_id)

        with self.engine.connect() as conn:
            try:
                conn.execute(stmt)
                conn.commit()
                return jsonify(message=f"Product ID {product_id} deleted successfully")

            except Exception as error:
                conn.rollback()
                return jsonify(error_message=f"Error deleting product ID {product_id}: {error}")