from ioc_container import ioc

def seed_admin():
    try:
        username = "diego"
        password = "123"

        hashed_password = ioc.ph.hash(password)
        result = ioc.users_repo.create_initial_admin(username, hashed_password)

        if result is not None:
            return f"Administrator created successfully. ID: {result}"
        else:
            return "Error creating Administrator"

    except Exception as error:
        return str(error)

if __name__ == "__main__":
    result = seed_admin()
    print(result)