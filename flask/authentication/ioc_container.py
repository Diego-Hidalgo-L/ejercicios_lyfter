from db import db_context
from jwt_manager import JWTManager
from repositories import UsersRepository

# Se encarga de todas las DEPENDENCIAS
class IocContainer:
    def __init__(self) -> None:
        self.db_context = db_context
        self.jwt_manager = JWTManager('trespatitos', 'HS256')
        self.users_repo = UsersRepository(self.db_context.engine)