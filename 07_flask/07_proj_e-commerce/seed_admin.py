from ioc_container import ioc
from db import User

def seed_admin():
    try:
        username = "diego"
        password = "123"
        email = "diego@gmail.com"
        full_name = "Diego Hidalgo"

        hashed_password = ioc.ph.hash(password)
        new_user = User(username=username, password=hashed_password, email=email, full_name=full_name, role='Administrator')
        result = new_user.add()

        if result is not None:
            return f"Administrator created successfully. ID: {result.id}"
        else:
            return "Error creating Administrator"

    except Exception as error:
        return str(error)

if __name__ == "__main__":
    result = seed_admin()
    print(result)