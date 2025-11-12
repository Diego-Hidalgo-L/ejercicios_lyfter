
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, request):
        pass


class AdminUser(User):
    def get_role(self):
        return "Administrator"
    
    def has_permission(self, permission):
            return True


class RegularUser(User):
    allowed_permissions = {"read"}
    
    def get_role(self):
        return "Regular User"
    
    def has_permission(self, permission):
        return permission in self.allowed_permissions


user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")

print(user1.has_permission("delete"))  
print(user2.has_permission("delete"))

print(user2.has_permission("read"))