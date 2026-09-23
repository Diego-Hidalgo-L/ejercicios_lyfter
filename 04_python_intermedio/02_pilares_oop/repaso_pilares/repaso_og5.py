
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass


class AdminUser(User):
    role = "Administrator"
    allowed_permissions = {"read", "edit", "delete", "share"} # esto es un set, no un dict. la búsqueda es más rápida.
    
    def has_permission(self, permission):
        return permission in self.allowed_permissions


class RegularUser(User):
    role = "Regular"
    allowed_permissions = {"read"} # esto es un set, no un dict. la búsqueda es más rápida.
    
    def has_permission(self, permission):
        return permission in self.allowed_permissions


def main():
    users = [
        AdminUser("Carlos"),
        RegularUser("Andrea")
]

    for user in users:
        print(f"{user.role} user '{user.name}' has permission to delete? {user.has_permission('delete')}")
        print(f"{user.role} user '{user.name}' has permission to read? {user.has_permission('read')}")



main()