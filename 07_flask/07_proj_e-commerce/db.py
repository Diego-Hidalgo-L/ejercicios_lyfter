from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship
from sqlalchemy import MetaData, Identity, ForeignKey, CheckConstraint, Integer, Float, String, Date
from sqlalchemy import select, func
from datetime import date

meta_obj = MetaData(schema="e_commerce")


class Base(DeclarativeBase):
    metadata = meta_obj


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(30), nullable=False)
    role: Mapped[str] = mapped_column(String(30), CheckConstraint("role in ('Administrator', 'User')"), nullable=False)

    invoices: Mapped[list["Invoice"]] = relationship(back_populates="user")

    # Methods:


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    entry_date: Mapped[date] = mapped_column(Date, nullable=False, default=date.today)
    stock: Mapped[int] = mapped_column(Integer)

    in_invoices: Mapped[list["InvoiceProduct"]] = relationship(back_populates="product")

    # Methods:


class Invoice(Base):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    purchase_date: Mapped[date] = mapped_column(Date, nullable=False, default=date.today)

    user: Mapped["User"] = relationship(back_populates=("invoices"))
    products: Mapped[list["Product"]] = relationship(back_populates="invoice")

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