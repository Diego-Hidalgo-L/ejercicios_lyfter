from db import db_context
from jwt_manager import JWTManager
from repositories import UsersRepository
from argon2 import PasswordHasher

# Se encarga de todas las DEPENDENCIAS
class IocContainer:
    def __init__(self) -> None:
        self.db_context = db_context
        self.jwt_manager = JWTManager()
        self.ph = PasswordHasher()
        self.users_repo = UsersRepository(self.db_context.engine)