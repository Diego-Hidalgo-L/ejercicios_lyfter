
user_logged_in = True

def requires_login(func):
    def wrapper(user):
        if user_logged_in == True:
                func(user)
        else:
            print("Usuario no autenticado")

    return wrapper


@requires_login
def view_profile(user):
    print(f"Mostrando perfil de usuario: '{user}'.")


view_profile("Diego")