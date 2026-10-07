from ioc_container import ioc
from db_engine import engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship
from sqlalchemy import MetaData, Identity, ForeignKey, CheckConstraint, Integer, Float, String, Date
from sqlalchemy import select, func
from datetime import date

meta_obj = MetaData(schema="e_commerce")

# Depende de cómo maneje el main.py tendré que agregar returns y return None's en todos los métodos.

class Base(DeclarativeBase):
    metadata = meta_obj


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(200), nullable=False)
    email: Mapped[str] = mapped_column(String(30), unique=True, nullable=False) # Hay que volver a crear las tablas para incluir 'email'
    full_name: Mapped[str] = mapped_column(String(30), nullable=False)
    role: Mapped[str] = mapped_column(String(30), CheckConstraint("role in ('Administrator', 'User')"), nullable=False)

    invoices: Mapped[list["Invoice"]] = relationship(back_populates="user")

    # Methods:
    def add_initial_admin(self):    # es necesario este método? No podría nada más usar el add(self) de abajo, aún para crear el Admin inicial?
        with Session(engine) as session:
            try:
                session.add(self)
                session.commit()
                print("Initial Administrator added successfully")

                session.refresh(self)
                return self

            except Exception as error:
                session.rollback()
                print("Error inserting initial Administrator into the database:", error)
                return None

    def add(self):
        with Session(engine) as session:
            try:
                session.add(self)
                session.commit()
                print("User added successfully")

                session.refresh(self)
                return self

            except Exception as error:
                session.rollback()
                print("Error adding user to the database:", error)
                return None

    @staticmethod
    def get_by_id(user_id):
        with Session(engine) as session:
            try:
                user = session.get(User, user_id) # ¿Por qué '.get()' aquí? --> "Dame el User cuyo primary key sea user_id."
                return user

            except Exception as error:
                session.rollback()
                print(f"Error getting user ID {user_id} from the database: {error}")
                return None

    @staticmethod
    def get_by_username(username):
        with Session(engine) as session:
            try:
                stmt = select(User).where(User.username == username)
                user = session.scalar(stmt)
                return user

            except Exception as error:
                session.rollback()
                print(f"Error getting user with username '{username}' from the database: {error}")

    def update(self, username=None, password=None, full_name=None): # 'role' solo permitido para Administrator?
        with Session(engine) as session:
            try:
                user = session.get(User, self.id) # vuelvo a obtener el objeto porque el del endpoint pertenece a otro session.

                if username is not None:
                    user.username = username

                if password is not None:
                    new_password = ioc.ph.hash(password)
                    user.password = new_password

                if full_name is not None:
                    user.full_name = full_name

                session.commit()
                print(f"User ID {user.id} updated successfully in the database")
                return True

            except Exception as error:
                session.rollback()
                print(f"Error updating user ID {self.id} on the database: {error}")
                return None

    def delete(self):
        with Session(engine) as session:
            try:
                user = session.get(User, self.id)

                if user:
                    session.delete(user)
                    session.commit()
                    print(f"User ID {user.id} deleted successfully")
                else:
                    print(f"User ID {self.id} not found")

            except Exception as error:
                session.rollback()
                print(f"Error deleting user ID {self.id} from the database:", error)


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    entry_date: Mapped[date] = mapped_column(Date, nullable=False, default=date.today)
    stock: Mapped[int] = mapped_column(Integer)

    in_invoices: Mapped[list["InvoiceProduct"]] = relationship(back_populates="product")

    # Methods:
    def add(self):
        with Session(engine) as session:
            try:
                session.add(self)
                session.commit()
                print("Product added successfully")

                session.refresh(self)
                return self

            except Exception as error:
                session.rollback()
                print(f"Error adding product to the database: {error}")

    def get(self):
        with Session(engine) as session:
            try:
                product = session.get(Product, self.id)       # Tal vez hay que más bien usar session.scalars(stmt).first()
                return product

            except Exception as error:
                session.rollback()
                print(f"Error getting product ID {self.id} from the database: {error}")

    def update(self, name=None, price=None, entry_date=None, stock=None):
        with Session(engine) as session:
            try:
                product = session.get(Product, self.id)

                if product:
                    if name is not None:
                        product.name = name

                    if price is not None:
                        product.price = price

                    if entry_date is not None:
                        product.entry_date = entry_date

                    if stock is not None:
                        product.stock = stock
                else:
                    print(f"Product ID {self.id} not found")

                session.commit()
                print(f"Product ID {product.id} updated successfully")

            except Exception as error:
                session.rollback()
                print(f"Error updating product ID {self.id} on the database: {error}")

    def delete(self):
        with Session(engine) as session:
            try:
                product = session.get(Product, self.id)

                if product:
                    session.delete(product)
                    session.commit()
                    print(f"Product ID {product.id} deleted successfully")
                else:
                    print(f"Product ID {self.id} not found")

            except Exception as error:
                session.rollback()
                print(f"Error deleting product ID {self.id} from the database: {error}")



class Invoice(Base):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    purchase_date: Mapped[date] = mapped_column(Date, nullable=False, default=date.today)

    user: Mapped["User"] = relationship(back_populates=("invoices"))
    products: Mapped[list["InvoiceProduct"]] = relationship(back_populates="invoice")

    # Methods:


class InvoiceProduct(Base):
    __tablename__ = "invoice_products"

    id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True)
    invoice_id: Mapped[int] = mapped_column(Integer, ForeignKey("invoices.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    total_price: Mapped[float] = mapped_column(Float, nullable=False)

    invoice: Mapped["Invoice"] = relationship(back_populates="products")
    product: Mapped["Product"] = relationship(back_populates="in_invoices")

    # Methods:

# IMPLEMENTAR + MODIFICAR:
# los métodos del repositorio anterior de authentication en estas clases.


# CREAR:
# tabla de my_cart que se borre al finalizar una compra, pero que se mantenga siempre y cuando la compra no se haya completado.


# CREAR:
# tabla de carritos/compras anteriores.