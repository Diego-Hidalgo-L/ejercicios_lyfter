from ioc_container import ioc
from db_engine import engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship
from sqlalchemy import MetaData, Identity, ForeignKey, CheckConstraint, Integer, Float, String, Date, Boolean, Index
from sqlalchemy import select, delete, func, text
from datetime import date

meta_obj = MetaData(schema="e_commerce")


class Base(DeclarativeBase):
    metadata = meta_obj


class User(Base):
    __tablename__ = "users"

    __table_args__ = (
        CheckConstraint("role IN ('Administrator', 'User')"),
    )

    id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(200), nullable=False)
    email: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(30), nullable=False)
    role: Mapped[str] = mapped_column(String(30), nullable=False)

    # Relationships:
    invoices: Mapped[list["Invoice"]] = relationship(back_populates="user")
    billing_addresses: Mapped[list["BillingAddress"]] = relationship(back_populates="user")
    payment_methods: Mapped[list["UserPaymentMethod"]] = relationship(back_populates="user")
    carts: Mapped[list["Cart"]] = relationship(back_populates="user")

    # Methods:
    def format_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "full_name": self.full_name,
            "role": self.role
        }

    @staticmethod
    def get_all():
        with Session(engine) as session:
            try:
                stmt = select(User)
                raw_users = session.scalars(stmt).all()
                users = [user.format_dict() for user in raw_users]

                return users

            except Exception as error:
                print(f"Error getting all users from the database: {error}")
                return False

    @staticmethod
    def get_by_id(user_id):
        with Session(engine) as session:
            try:
                user = session.get(User, user_id) # ¿Por qué '.get()' aquí? --> "Dame el User cuyo primary key sea user_id."
                return user

            except Exception as error:
                print(f"Error getting user ID {user_id} from the database: {error}")
                return False

    @staticmethod
    def get_by_username(username):
        with Session(engine) as session:
            try:
                stmt = select(User).where(User.username == username)
                user = session.scalar(stmt)
                return user

            except Exception as error:
                print(f"Error getting user with username '{username}' from the database: {error}")
                return False

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
                return False

    def add(self):
        with Session(engine) as session:
            try:
                session.add(self)
                session.commit()
                print("User added successfully to the database")

                session.refresh(self)
                return self

            except Exception as error:
                session.rollback()
                print("Error adding user to the database:", error)
                return False

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
                return False

    def delete(self):
        with Session(engine) as session:
            try:
                user = session.get(User, self.id)

                session.delete(user)
                session.commit()
                print(f"User ID {user.id} deleted successfully from the database")
                return True

            except Exception as error:
                session.rollback()
                print(f"Error deleting user ID {self.id} from the database:", error)
                return False


class BillingAddress(Base):
    __tablename__ = "billing_addresses"

    id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    address: Mapped[str] = mapped_column(String(200), nullable=False)

    # Relationships:
    user: Mapped["User"] = relationship(back_populates="billing_addresses")
    invoices: Mapped[list["Invoice"]] = relationship(back_populates="billing_address")

    # Methods:
    def format_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "address": self.address
        }

    @staticmethod
    def get_all_by_user_id(user_id):
        with Session(engine) as session:
            try:
                stmt = select(BillingAddress).where(BillingAddress.user_id == user_id)
                raw_billing_addresses = session.scalars(stmt).all()
                billing_addresses = [billing_address.format_dict() for billing_address in raw_billing_addresses]

                return billing_addresses

            except Exception as error:
                print(f"Error getting user's billing addresses (ID: {user_id}): {error}")
                return False

    @staticmethod
    def get_by_id(billing_id):
        with Session(engine) as session:
            try:
                billing_address = session.get(BillingAddress, billing_id)
                return billing_address

            except Exception as error:
                print(f"Error getting user's billing addresses (ID: {billing_id}): {error}")
                return False

    def add(self):
        with Session(engine) as session:
            try:
                session.add(self)
                session.commit()
                print("Billing address added successfully to the database")

                session.refresh(self)
                return self

            except Exception as error:
                session.rollback()
                print(f"Error adding product to the database: {error}")
                return False

    def update(self, new_address):
        with Session(engine) as session:
            try:
                my_address = session.get(BillingAddress, self.id)
                my_address.address = new_address

                session.commit()
                print(f"Billing address ID {my_address.id} updated successfully in the database")
                return True

            except Exception as error:
                session.rollback()
                print(f"Error updating billing address ID {self.id} on the database: {error}")
                return False

    def delete(self):
        with Session(engine) as session:
            try:
                my_address = session.get(BillingAddress, self.id)

                session.delete(my_address)
                session.commit()
                print(f"Billing address ID {my_address.id} deleted successfully from the database")
                return True

            except Exception as error:
                session.rollback()
                print(f"Error updating billing address ID {self.id} on the database: {error}")
                return False


class PaymentMethod(Base):
    __tablename__ = "payment_methods"

    __table_args__ = (
        CheckConstraint("method IN ('Credit/Debit Card', 'Transfer', 'PayPal')"),
    )

    id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True)
    method: Mapped[str] = mapped_column(String(20), nullable=False)

    # Relationships:
    user_payment_methods: Mapped[list["UserPaymentMethod"]] = relationship(back_populates="payment_method")

    # Methods
    def format_dict(self):
        return {
            "id": self.id,
            "method": self.method
        }

    @staticmethod
    def get_all():
        pass

    def add(self):
        with Session(engine) as session:
            try:
                session.add(self)
                session.commit()
                print("Payment method added successfully to the database")

                session.refresh(self)
                return self

            except Exception as error:
                session.rollback()
                print(f"Error adding payment method to the database: {error}")
                return False


class UserPaymentMethod(Base):      # LINK TABLE N:N | Users:PaymentMethods
    __tablename__ = "user_payment_methods"

    __table_args__ = (
        Index("uq_one_default_method_per_user", "user_id", unique=True, postgresql_where=text("is_default = 'True'")),
    )

    id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    payment_method_id: Mapped[int] = mapped_column(Integer, ForeignKey("payment_methods.id"), nullable=False)
    alias: Mapped[str] = mapped_column(String(50), nullable=True)
    is_default: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    # Relationships:
    user: Mapped["User"] = relationship(back_populates="payment_methods")
    invoices: Mapped[list["Invoice"]] = relationship(back_populates="user_payment_method")
    payment_method: Mapped["PaymentMethod"] = relationship(back_populates="user_payment_methods")

    # Methods:
    def format_dict(self, method):
        return {
            "id": self.id,
            "method": method,
            "method_id": self.payment_method_id,
            "alias": self.alias,
            "is_default": self.is_default
        }

    def add(self):
        with Session(engine) as session:
            try:
                session.add(self)
                session.commit()
                session.refresh(self)
                print(f"Payment method added for user ID {self.id} successfully to the database")
                
                return self

            except Exception as error:
                session.rollback()
                print(f"Error adding payment method to the database: {error}")
                return False

    @staticmethod
    def get_all_by_user_id(user_id):
        with Session(engine) as session:
            try:
                stmt = select(UserPaymentMethod).where(UserPaymentMethod.user_id == user_id)
                raw_payment_methods = session.scalars(stmt).all()

                payment_methods = []

                for payment_method in raw_payment_methods:
                    method = session.get(PaymentMethod, payment_method.payment_method_id)
                    payment_methods.append(payment_method.format_dict(method.method))

                print(payment_methods)
                return payment_methods

            except Exception as error:
                print(f"Error getting user's payment methods (user ID: {user_id}): {error}")
                return False

    @staticmethod
    def get_by_id(payment_id):
        with Session(engine) as session:
            try:
                my_payment_method = session.get(UserPaymentMethod, payment_id)
                return my_payment_method

            except Exception as error:
                print(f"Error getting user's payment method ID: {payment_id}: {error}")
                return False

    def update(self, new_alias, is_default):
        with Session(engine) as session:
            try:
                my_payment_method = session.get(UserPaymentMethod, self.id)

                if new_alias is not None:
                    my_payment_method.alias = new_alias

                if is_default is not None:
                    my_payment_method.is_default = is_default

                session.commit()
                print(f"Payment method ID {my_payment_method.id} updated successfully in the database")
                return True

            except Exception as error:
                session.rollback()
                print(f"Error updating payment method ID {self.id} on the database: {error}")
                return False

    def delete(self):
        with Session(engine) as session:
            try:
                my_payment_method = session.get(UserPaymentMethod, self.id)

                session.delete(my_payment_method)
                session.commit()
                print(f"Payment method ID {my_payment_method.id} deleted successfully from the database")
                return True

            except Exception as error:
                session.rollback()
                print(f"Error deleting payment method ID {self.id} from the database: {error}")
                return False


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    entry_date: Mapped[date] = mapped_column(Date, nullable=False, default=date.today)
    stock: Mapped[int] = mapped_column(Integer)

    # Relationships:
    in_invoices: Mapped[list["InvoiceProduct"]] = relationship(back_populates="product")
    in_carts: Mapped[list["CartProduct"]] = relationship(back_populates="product")

    # Methods:
    def format_dict(self):
        return {
                "id": self.id,
                "name": self.name,
                "price": self.price,
                "entry_date": str(self.entry_date),
                "stock": self.stock
            }

    @staticmethod
    def get_all():
        with Session(engine) as session:
            try:
                stmt = select(Product)
                raw_products = session.scalars(stmt).all()
                products = [product.format_dict() for product in raw_products]

                return products

            except Exception as error:
                print(f"Error getting all products from the database: {error}")
                return False

    @staticmethod
    def get_by_id(product_id):
        with Session(engine) as session:
            try:
                product = session.get(Product, product_id)
                return product

            except Exception as error:
                print(f"Error getting product ID {product_id} from the database: {error}")
                return False

    def add(self):
        with Session(engine) as session:
            try:
                session.add(self)
                session.commit()
                print("Product added successfully to the database")

                session.refresh(self)
                return self

            except Exception as error:
                session.rollback()
                print(f"Error adding product to the database: {error}")
                return True

    def update(self, name=None, price=None, entry_date=None, stock=None):
        with Session(engine) as session:
            try:
                product = session.get(Product, self.id)

                if name is not None:
                    product.name = name

                if price is not None:
                    product.price = price

                if entry_date is not None:
                    product.entry_date = entry_date

                if stock is not None:
                    product.stock = stock

                session.commit()
                print(f"Product ID {product.id} updated successfully in the database")
                return True

            except Exception as error:
                session.rollback()
                print(f"Error updating product ID {self.id} on the database: {error}")
                return False

    def delete(self):
        with Session(engine) as session:
            try:
                product = session.get(Product, self.id)

                session.delete(product)
                session.commit()
                print(f"Product ID {product.id} deleted successfully from the database")
                return True

            except Exception as error:
                session.rollback()
                print(f"Error deleting product ID {self.id} from the database: {error}")
                return False


class Cart(Base):
    __tablename__ = "carts"

    __table_args__ = (
        CheckConstraint("status IN ('Active', 'Completed', 'Abandoned')"),
        Index("uq_one_active_cart_per_user", "user_id", unique=True, postgresql_where=text("status = 'Active'"))
    )

    id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    creation_date: Mapped[date] = mapped_column(Date, nullable=False, default=date.today)
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="Active")

    # Relationships:
    user: Mapped["User"] = relationship(back_populates="carts")
    cart_products: Mapped[list["CartProduct"]] = relationship(back_populates="cart")

    # Methods:
    def format_dict(self, cart_products):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "creation_date": self.creation_date,
            "cart_products": cart_products,
            "status": self.status
        }

    @staticmethod
    def get_all_by_user_id(user_id):
        with Session(engine) as session:
            try:
                stmt = select(Cart)
                raw_carts = session.scalars(stmt).all()

                carts_list = []

                for raw_cart in raw_carts:
                    cart_products = CartProduct.get_by_cart_id(raw_cart.id)
                    cart = raw_cart.format_dict(cart_products)
                    carts_list.append(cart)

                return carts_list

            except Exception as error:
                session.rollback()
                print(f"Error getting user's carts (user ID: {user_id}): {error}")
                return False

    @staticmethod
    def get_or_create_active_cart(user_id):
        with Session(engine) as session:
            try:
                stmt = select(Cart).where(Cart.user_id == user_id, Cart.status == "Active")
                cart = session.scalar(stmt)

                if cart is None:
                    cart = Cart(user_id=user_id, creation_date=date.today(), status="Active")
                    session.add(cart)
                    session.commit()
                    session.refresh(cart)

                return cart

            except Exception as error:
                session.rollback()
                print(f"Error getting active cart from the database: {error}"), 500
                return False

    @staticmethod
    def get_by_id_obj(cart_id):
        with Session(engine) as session:
            try:
                cart = session.get(Cart, cart_id)
                return cart

            except Exception as error:
                session.rollback()
                print(f"Error getting cart ID {cart_id}: {error}")
                return False 

    @staticmethod
    def get_by_id_dict(cart_id):
        with Session(engine) as session:
            try:
                cart = session.get(Cart, cart_id)

                if cart is None:
                    return None
                else:
                    cart_products = [product.format_dict() for product in cart.cart_products]
                    return cart.format_dict(cart_products)
                
            except Exception as error:
                session.rollback()
                print(f"Error getting cart ID {cart_id}: {error}")
                return False 

    def add(self):
        with Session(engine) as session:
            try:
                session.add(self)
                session.commit()
                print("Cart added successfully to the database")

                session.refresh(self)
                return self
            
            except Exception as error:
                session.rollback()
                print(f"Error adding cart to the database: {error}")
                return False

    def update(self, cart_products, status):
        with Session(engine) as session:
            try:
                cart = session.get(Cart, self.id)

                # Delete cart_products belonging to target cart:
                if cart_products is not None:
                    stmt = delete(CartProduct).where(CartProduct.cart_id == cart.id)
                    session.execute(stmt)

                    # Ingreso nuevos cart_products:
                    for product in cart_products:
                        new_product = CartProduct(cart_id=cart.id, product_id=product.get('product_id'), quantity=product.get('quantity'), total_price=product.get('total_price'))
                        session.add(new_product)

                # Modifico 'status':
                if status is not None:
                    cart.status = status

                # Commit:
                session.commit()
                print("Cart products updated successfully")
                return True

            except Exception as error:
                session.rollback()
                print(f"Error updating cart products in the database: {error}")
                return False

    def delete(self):
        with Session(engine) as session:
            try:
                cart = session.get(Cart, self.id)

                session.delete(cart)
                session.commit()
                print(f"Cart ID {cart.id} successfully deleted from the database")
                return True

            except Exception as error:
                session.rollback()
                print(f"Error deleting cart ID {self.id} from the database: {error}")
                return False


class CartProduct(Base):
    __tablename__ = "cart_products"

    id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True)
    cart_id: Mapped[int] = mapped_column(Integer, ForeignKey("carts.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    total_price: Mapped[float] = mapped_column(Float, nullable=False)

    # Relationships:
    cart: Mapped["Cart"] = relationship(back_populates="cart_products")
    product: Mapped[list["Product"]] = relationship(back_populates="in_carts")

    # Methods:
    def format_dict(self):
        return {
            "product_id": self.product_id,
            "quantity": self.quantity,
            "total_price": self.total_price
        }

    @staticmethod
    def get_by_cart_id(cart_id):
        with Session(engine) as session:
            try:
                stmt = select(CartProduct).where(CartProduct.cart_id == cart_id)
                raw_cart_products = session.scalars(stmt).all()
                cart_products = [cart_product.format_dict() for cart_product in raw_cart_products]

                return cart_products

            except Exception as error:
                session.rollback()
                print(f"Error getting products for cart ID {cart_id} from the database: {error}")
                return False

    def add(self):
        with Session(engine) as session:
            try:
                session.add(self)
                session.commit()

                session.flush()
                print(f"Cart product ID {self.id} added successfully to the database")
                return self

            except Exception as error:
                session.rollback()
                print(f"Error adding cart products to the database: {error}")
                return False

    @staticmethod
    def delete(cart_id):
        with Session(engine) as session:
            try:
                stmt = delete(CartProduct).where(CartProduct.cart_id == cart_id)
                session.execute(stmt)

                session.commit()
                print("Cart products deleted successfully")
                return True

            except Exception as error:
                session.rollback()
                print(f"Error deleting products for cart ID {cart_id} from the database: {error}")
                return False


class Invoice(Base):
    __tablename__ = "invoices"

    __table_args__ = (
            CheckConstraint("status IN ('Completed', 'Returned')"),
    )

    id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    purchase_date: Mapped[date] = mapped_column(Date, nullable=False, default=date.today)
    billing_address_id: Mapped[int] = mapped_column(Integer, ForeignKey("billing_addresses.id"), nullable=False)
    user_payment_method_id: Mapped[int] = mapped_column(Integer, ForeignKey("user_payment_methods.id"), nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False)

    # Relationships:
    user: Mapped["User"] = relationship(back_populates="invoices")
    billing_address: Mapped["BillingAddress"] = relationship(back_populates="invoices")
    user_payment_method: Mapped["UserPaymentMethod"] = relationship(back_populates="invoices")
    products: Mapped[list["InvoiceProduct"]] = relationship(back_populates="invoice")

    # Methods:
    def format_dict(self, billing_address, user_payment_method, products):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "purchase_date": self.purchase_date,
            "billing_address": billing_address,
            "user_payment_method": user_payment_method,
            "products": products,
            "status": self.status
        }

    @staticmethod
    def get_all_by_user_id(user_id):
        with Session(engine) as session:
            try:
                stmt = select(Invoice).where(Invoice.user_id == user_id)
                raw_invoices = session.scalars(stmt).all()

                invoices_list = []
                
                for raw_invoice in raw_invoices:
                    billing_address = BillingAddress.get_by_id(raw_invoice.billing_address_id).address
                    user_payment_method = UserPaymentMethod.get_by_id(raw_invoice.user_payment_method_id).alias
                    products = InvoiceProduct.get_by_invoice_id(raw_invoice.id) # lista de products
                    invoices_list.append(raw_invoice.format_dict(billing_address, user_payment_method, products))

                return invoices_list

            except Exception as error:
                print(f"Error getting user's invoices from the database (ID: {user_id}): {error}")
                return False

    @staticmethod
    def get_by_id(invoice_id):
        with Session(engine) as session:
            try:
                invoice = session.get(Invoice, invoice_id)
                return invoice

            except Exception as error:
                print(f"Error getting invoice ID {invoice_id} from the database: {error}")
                return False

    def add(self):
        with Session(engine) as session:
            try:
                session.add(self)
                session.commit()
                print("Invoice added successfully to the database")

                session.refresh(self)
                return self

            except Exception as error:
                session.rollback()
                print(f"Error adding invoice to the database: {error}")
                return False


class InvoiceProduct(Base):
    __tablename__ = "invoice_products"

    id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True)
    invoice_id: Mapped[int] = mapped_column(Integer, ForeignKey("invoices.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    total_price: Mapped[float] = mapped_column(Float, nullable=False)

    # Relationships:
    invoice: Mapped["Invoice"] = relationship(back_populates="products")
    product: Mapped["Product"] = relationship(back_populates="in_invoices")

    # Methods:
    def format_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "total_price": self.total_price
        }

    def add(self):
        with Session(engine) as session:
            try:
                session.add(self)               
                session.commit()
                print("Invoice products added successfully to the database")

                session.refresh(self)
                return self

            except Exception as error:
                session.rollback()
                print(f"Error insert invoice products into the database: {error}")
                return False

    @staticmethod
    def get_by_invoice_id(invoice_id):
        with Session(engine) as session:
            try:
                stmt = select(InvoiceProduct).where(InvoiceProduct.invoice_id == invoice_id)
                raw_invoice_products = session.scalars(stmt).all()
                invoice_products = [inv_product.format_dict() for inv_product in raw_invoice_products]

                return invoice_products

            except Exception as error:
                print(f"Error getting invoice products from the database: {error}")
                return False


# CREAR:
# tabla de my_cart que se borre al finalizar una compra, pero que se mantenga siempre y cuando la compra no se haya completado.


# CREAR:
# tabla de carritos/compras anteriores.