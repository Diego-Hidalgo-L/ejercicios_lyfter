from db import db_context
from jwt_manager import JWTManager
from repositories import UsersRepository, ProductsRepository, InvoicesRepository, InvoiceProductsRepository
from argon2 import PasswordHasher

# Se encarga de todas las DEPENDENCIAS
class IocContainer:
    def __init__(self) -> None:
        self.db_context = db_context
        self.jwt_manager = JWTManager()
        self.ph = PasswordHasher()

        # Repos:
        self.users_repo = UsersRepository(self.db_context.engine)
        self.products_repo = ProductsRepository(self.db_context.engine)
        self.invoices_repo = InvoicesRepository(self.db_context.engine)
        self.inv_products_repo = InvoiceProductsRepository(self.db_context.engine)

ioc = IocContainer()