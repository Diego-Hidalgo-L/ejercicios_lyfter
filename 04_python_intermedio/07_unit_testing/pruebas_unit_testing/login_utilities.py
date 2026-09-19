
def try_login(email, password):
    if email == "a@gmail.com" and password == "123":
        return True
    else:
        raise ValueError("These credentials are incorrect!")
    
import sys
print(sys.executable, sys.version)