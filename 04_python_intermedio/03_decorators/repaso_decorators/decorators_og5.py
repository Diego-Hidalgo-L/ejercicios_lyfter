
def requires_login(func):
    def wrapper(*args, **kwargs):
        try:
            if user_logged_in:
                return func(*args, **kwargs)
            else:
                raise Exception("Usuario no autenticado")
        except Exception as e:
            print(e)
    
    return wrapper


user_logged_in = True

@requires_login
def view_profile(user):
    print(f"Mostrando perfil del usuario: {user}")


view_profile("Diego")