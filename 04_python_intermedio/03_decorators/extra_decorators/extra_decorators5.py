
from functools import wraps

user = {"authenticated": True}

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not user["authenticated"]:
            print("Access Denied")
            return
        else:
            return func(*args, **kwargs)
        
    return wrapper


@authenticate
def secret_function():
    """This function prints a secret."""
    print("Top secret data.")


secret_function()
print(secret_function.__name__)
print(secret_function.__doc__)