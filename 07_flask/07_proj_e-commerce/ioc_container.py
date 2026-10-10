from jwt_manager import JWTManager
# from cache import CacheManager
# from credentials.redis_creds import host, port, password
from argon2 import PasswordHasher


class IocContainer:
    def __init__(self) -> None:
        self.jwt_manager = JWTManager()
        self.ph = PasswordHasher()
        # self.cache_manager = CacheManager(host=host, port=port, password=password)


ioc = IocContainer()