
from functools import wraps
from datetime import date

class User:
    def __init__(self, name, date_of_birth, role=('admin', 'user')):
        self.name = name
        self.date_of_birth = date_of_birth
        self.role = role

    @property
    def age(self):
        today = date.today()
        return (today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)))


def requires_adult(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = args[0]

        if user.age >= 18:
            return func(*args, **kwargs)
        else:
            raise PermissionError(f"User {user.name} is underage")
    
    return wrapper


def requires_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user = args[0]

            if user.role == role:
                return func(*args, **kwargs)
            else:
                raise PermissionError(f"Role '{role}' required")

        return wrapper
    
    return decorator


@requires_adult
@requires_role('admin')
def delete_records(user):
    return f"Records deleted by {user.name}"


@requires_adult
def view_content(user):
    return f"Content viewed by {user.name}"


def main():
    user1 = User("Diego", date(1997, 5, 25), 'admin')
    user2 = User("Mateo", date(2014, 12, 19), 'user')

    users = [user1, user2]
    actions = [delete_records, view_content]

    for user in users:
        for action in actions:
            try:
                print(action(user))

            except PermissionError as e:
                print(str(e))


main()