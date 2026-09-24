from db import db_context
from sqlalchemy import select, insert, update, delete
from datetime import date

# Se encarga de los queries de las tablas de nuestra base de datos.

class UsersRepository:
    def __init__(self, engine):
        self.engine = engine

    def create_initial_admin(self, username, password):
        with self.engine.connect() as conn:
            try:
                stmt = insert(db_context.users).returning(db_context.users.c.id).values(username=username, password=password, role="Administrator")
                result = conn.execute(stmt)
                admin_id = result.scalar_one_or_none()
                # 'result' es una lista con una tupla adentro, por eso antes usaba admin_id = result.all()[0][0]
                # result.scalar_one_or_none() --> "Dame el único valor escalar que devolvió esta consulta, o None si no hubo ninguno."
                
                if admin_id is None:
                    return None
                
                conn.commit()
                print("User inserted successfully")

                return admin_id

            except Exception as error:
                conn.rollback()
                print("Error inserting initial Administrator into the database:", error)
                return None

    def insert(self, username, password):
        with self.engine.connect() as conn:
            try:
                stmt = insert(db_context.users).returning(db_context.users.c.id).values(username=username, password=password, role="User")
                result = conn.execute(stmt)
                new_user_id = result.scalar_one_or_none()
                
                if new_user_id is None:
                    return None
                
                conn.commit()
                print("User inserted successfully")

                return new_user_id

            except Exception as error:
                conn.rollback()
                print("Error inserting user into the database:", error)
                return None

    def get_by_username(self, username):
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

    def get_by_user_id(self, user_id):
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

    def update(self, user_id, username=None, password=None): # (, role=None) --> SOLO ADMINISTRATOR
        with self.engine.connect() as conn:
            try:
                if username is not None:
                    stmt = update(db_context.users).where(db_context.users.c.id==user_id).values(username=username)
                    conn.execute(stmt)

                if password is not None:
                    stmt = update(db_context.users).where(db_context.users.c.id==user_id).values(password=password)
                    conn.execute(stmt)

                # if role is not None:
                #     stmt = update(db_context.users).where(db_context.users.c.id==user_id).values(role=role) # --> SOLO ADMINISTRATOR
                #     conn.execute(stmt)

                conn.commit()
                print(f"User ID {user_id} updated successfully")
                return True

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
                return True

            except Exception as error:
                conn.rollback()
                print(f"Error deleting user ID {user_id}: {error}")
                return None


# ------------- EXTRA: -------------
class ContactsRepository:
    def __init__(self, engine):
        self.engine = engine

    def insert(self, name, user_id, phone, email):
        with self.engine.connect() as conn:
            try:
                stmt = insert(db_context.contacts).returning(db_context.contacts.c.user_id).values(name=name, user_id=user_id, phone=phone, email=email)
                result = conn.execute(stmt)
                new_contact_user_id = result.all()[0][0]

                conn.commit()
                print("Contact inserted successfully")

                return new_contact_user_id

            except Exception as error:
                conn.rollback()
                print(f"Error inserting contact into the database: {error}")
                return None

    def get_by_contact_id(self, contact_id):
        with self.engine.connect() as conn:
            try:
                stmt = select(db_context.contacts).where(db_context.contacts.c.id==contact_id)
                result = conn.execute(stmt)
                contact_result = result.all()

                if len(contact_result) == 0:
                    return None
                else:
                    contact = contact_result[0]
                    format_contact = {"id":contact[0], "user_id":contact[1], "name":contact[2], "phone":contact[3], "email":contact[4]}
                    return format_contact

            except Exception as error:
                print(f"Error getting contact ID {contact_id}: {error}")
                return None

    def get_by_user_id(self, user_id):
        with self.engine.connect() as conn:
            try:
                stmt = select(db_context.contacts).where(db_context.contacts.c.user_id==user_id)
                result = conn.execute(stmt)
                contact_result = result.all()

                if len(contact_result) == 0:
                    return None
                else:
                    contact_list = []

                    for contact in contact_result:
                        contact_dict = {
                            "id":contact[0],
                            "user_id":contact[1],
                            "name":contact[2],
                            "phone":contact[3],
                            "email":contact[4]
                        }
                        contact_list.append(contact_dict)

                    return contact_list

            except Exception as error:
                print(f"Error getting contact from user ID {user_id}: {error}")
                return None

    def get_all(self):
        with self.engine.connect() as conn:
            try:
                stmt = select(db_context.contacts)
                result = conn.execute(stmt)
                contacts_raw = result.all()

                if len(contacts_raw) == 0:
                    return None
                else:
                    all_contacts = []

                    for contact in contacts_raw:
                        contact_dict = {
                            "id": contact[0],
                            "user_id": contact[1],
                            "name": contact[2],
                            "phone": contact[3],
                            "email": contact[4]
                        }
                        all_contacts.append(contact_dict)

                return all_contacts

            except Exception as error:
                conn.rollback()
                print(f"Error getting all contacts from the database: {error}")
                return None

    def update(self, contact_id, name=None, phone=None, email=None):
        with self.engine.connect() as conn:
            try:
                if name is not None:
                    stmt = update(db_context.contacts).where(db_context.contacts.c.id==contact_id).values(name=name)
                    conn.execute(stmt)

                if phone is not None:
                    stmt = update(db_context.contacts).where(db_context.contacts.c.id==contact_id).values(phone=phone)
                    conn.execute(stmt)

                if email is not None:
                    stmt = update(db_context.contacts).where(db_context.contacts.c.id==contact_id).values(email=email)
                    conn.execute(stmt)

                conn.commit()
                print(f"Contact ID {contact_id} updated successfully")
                return True

            except Exception as error:
                conn.rollback()
                print(f"Error updating contact ID {contact_id}: {error}")
                return None

    def delete(self, contact_id):
        with self.engine.connect() as conn:
            try:
                stmt = delete(db_context.contacts).where(db_context.contacts.c.id==contact_id)
                conn.execute(stmt)

                conn.commit()
                print(f"Contact ID {contact_id} deleted successfully")
                return True

            except Exception as error:
                conn.rollback()
                print(f"Error deleting contact ID {contact_id}: {error}")
                return None


class LoginHistory:
    def __init__(self, engine):
        self.engine = engine

    def register_login(self, user_id, now, ip, status):
        with self.engine.connect() as conn:
            try:
                stmt = insert(db_context.login_history).returning(db_context.login_history.c.id).values(user_id=user_id, datetime=now, ip=ip, status=status)
                result = conn.execute(stmt)
                new_login_id = result.all()[0][0]

                conn.commit()
                print("Login registered successfully")

                return new_login_id

            except Exception as error:
                conn.rollback()
                print(f"Error registering login into the database: {error}")
                return None

    def get_history(self):
        with self.engine.connect() as conn:
            try:
                stmt = select(db_context.login_history)
                result = conn.execute(stmt)
                history_raw = result.all()

                if len(history_raw) == 0:
                    return None
                else:
                    history = []

                    for record in history_raw:
                        record_dict = {
                            "id": record[0],
                            "user_id": record[1],
                            "datetime": record[2],
                            "ip": record[3],
                            "status": record[4]
                        }
                        history.append(record_dict)

                return history

            except Exception as error:
                conn.rollback()
                print(f"Error getting login history from the database: {error}")
                return None

# ------------- FIN EXTRA -------------


class ProductsRepository:
    def __init__(self, engine):
        self.engine = engine

    def insert(self, name, price, entry_date, stock):
        with self.engine.connect() as conn:
            try:
                stmt = insert(db_context.products).returning(db_context.products.c.name).values(name=name, price=price, entry_date=entry_date, stock=stock)
                result = conn.execute(stmt)
                new_product_name = result.scalar_one_or_none()

                conn.commit()
                print("Product inserted successfully")

                return new_product_name

            except Exception as error:
                conn.rollback()
                print(f"Error inserting product into the database: {error}")
                return None

    def get_by_product_id(self, product_id):
        with self.engine.connect() as conn:
            try:
                stmt = select(db_context.products).where(db_context.products.c.id == product_id)
                result = conn.execute(stmt)
                product = result.all()

                if len(product) == 0:
                    return None
                else:
                    return product[0] # Sacamos la tupla de la lista retornada

            except Exception as error:
                print(f"Error getting product ID {product_id}: {error}")
                return None

    def update(self, product_id, name=None, price=None, entry_date=None, stock=None):
        with self.engine.connect() as conn:
            try:
                if name is not None:
                    stmt = update(db_context.products).where(db_context.products.c.id==product_id).values(name=name)
                    conn.execute(stmt)

                if price is not None:
                    stmt = update(db_context.products).where(db_context.products.c.id==product_id).values(price=price)
                    conn.execute(stmt)

                if entry_date is not None:
                    stmt = update(db_context.products).where(db_context.products.c.id==product_id).values(entry_date=entry_date)
                    conn.execute(stmt)

                if stock is not None:
                    stmt = update(db_context.products).where(db_context.products.c.id==product_id).values(stock=stock)
                    conn.execute(stmt)

                conn.commit()
                print(f"Product ID {product_id} updated successfully")
                return True

            except Exception as error:
                conn.rollback()
                print(f"Error updating product ID {product_id}: {error}")
                return None

    def delete(self, product_id):
        with self.engine.connect() as conn:
            try:
                stmt = delete(db_context.products).where(db_context.products.c.id==product_id)
                conn.execute(stmt)

                conn.commit()
                print(f"Product ID {product_id} deleted successfully")
                return True

            except Exception as error:
                conn.rollback()
                print(f"Error deleting product ID {product_id}: {error}")
                return None


class InvoicesRepository:
    def __init__(self, engine):
        self.engine = engine

    def insert(self, user_id, purchase_date):
        with self.engine.connect() as conn:
            try:
                stmt = insert(db_context.invoices).returning(db_context.invoices.c.id).values(user_id=user_id, purchase_date=purchase_date)
                result = conn.execute(stmt)
                invoice_id = result.scalar_one_or_none()

                if invoice_id is None:
                    return None

                conn.commit()
                print("Invoice inserted successfully")

                return invoice_id

            except Exception as error:
                conn.rollback()
                print(f"Error inserting invoice into the database: {error}")
                return None

    def get_invoices(self, user_id): # Después implementar filters
        with self.engine.connect() as conn:
            try:
                stmt = select(db_context.invoices).where(db_context.invoices.c.user_id==user_id)
                result = conn.execute(stmt) # tengo que convertir este resultado (lista de tuplas) en una lista de diccionarios
                invoices_result = result.all()

                if len(invoices_result) == 0:
                    return None
                else:
                    invoices_list = []

                    for invoice in invoices_result: # Hay algún lugar de donde pueda obtener estos keys sin tener que hacerles hardcode?
                        invoice_products = InvoiceProductsRepository.get_by_invoice_id(self, invoice[0])
                        inv_dict = { # Podría hacer un nesting de otro loop para iterar los valores dentro de la tupla
                            "id": invoice[0],
                            "user_id": invoice[1],
                            "purchase_date": invoice[2],
                            "invoice_products": invoice_products
                        }
                        invoices_list.append(inv_dict)

                    return invoices_list

            except Exception as error:
                conn.rollback()
                print(f"Error getting user's invoices: {error}")
                return None


class InvoiceProductsRepository:
    def __init__(self, engine):
        self.engine = engine

    def insert(self, invoice_id, product_id, quantity, total_price):
        with self.engine.connect() as conn:
            try:
                stmt = insert(db_context.invoice_products).values(invoice_id=invoice_id, product_id=product_id, quantity=quantity, total_price=total_price)
                conn.execute(stmt)

                conn.commit()
                print("Invoice products inserted successfully")
                return True

            except Exception as error:
                conn.rollback()
                print(f"Error insert invoice products into the database: {error}")
                return None

    def get_by_invoice_id(self, invoice_id):
        with self.engine.connect() as conn:
            try:
                stmt = select(db_context.invoice_products).where(db_context.invoice_products.c.invoice_id==invoice_id)
                result = conn.execute(stmt)
                invoice_result = result.all()
                
                if len(invoice_result) == 0:
                    return None
                else:
                    invoice_products = []

                    for product in invoice_result:
                        products_dict = {
                            "product_id": product[2],
                            "quantity": product[3],
                            "total_price": product[4]
                        }

                        invoice_products.append(products_dict)

                    return invoice_products

            except Exception as error:
                conn.rollback()
                print(f"Error getting invoice products from the database: {error}")
                return None


class TransactionsRepository:
    def __init__(self, engine):
        self.engine = engine

    def purchase(self, user_id, purchase_date, invoice_products):
        try:
            available_stock_list = []

            # Verifico stock:
            for product in invoice_products:
                product_id = product.get('product_id')
                purchase_quantity = product.get('quantity')
                got_product = ProductsRepository.get_by_product_id(self, product_id)
                available_stock = got_product[4]

                if available_stock < purchase_quantity:
                    return f"Insufficient stock for product ID {product_id} (Desired purchase quantity: {purchase_quantity} - Available stock: {available_stock}).", 400

                available_stock_list.append(available_stock)

            # Si todo el stock está bien, creo el invoice:
            invoice_id = InvoicesRepository.insert(self, user_id, purchase_date)

            if invoice_id is None:
                return "Error creating invoice", 500

            # Insert en loop en tabla invoice_products:
            for i, product in enumerate(invoice_products):
                insert_result = InvoiceProductsRepository.insert(self, invoice_id, product.get('product_id'), product.get('quantity'), product.get('total_price'))

                if insert_result is None:
                    return f"Error inserting product ID {product.get('product_id')} into invoice", 500

                available_stock = available_stock_list[i]
                stock_result = ProductsRepository.update(self, product.get('product_id'), stock=(available_stock-product.get('quantity')))

                if stock_result is None:
                    return "Error subtracting purchased quantity from available stock", 500

            return True, 201

        except Exception as error:
            print(error)
            return f"Error inserting purchase into the database: {error}", 500