
user_logged_in = False

def requires_login(func):
    def wrapper(*args, **kwargs):
        try:
            if user_logged_in == True:
                return func(*args, *kwargs.values())
            else:
                raise Exception
        except Exception:
            print("Error: Usuario no autenticado.")

    return wrapper


@requires_login
def view_profile(user):
    print(f"Mostrando perfil de usuario: '{user}'.")


view_profile("Diego")