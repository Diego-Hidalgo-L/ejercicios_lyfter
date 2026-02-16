
def search_key(user):
    while True:
        try:
            key = input("Ingres el key que desea buscar: ")
            return user[key]
        except KeyError:
            print(f"El key '{key}' no existe. Intente de nuevo.")


def main():
    user = {
    "name": "Ana",
    "email": "ana@email.com"
}
    result = search_key(user)
    print(result)


main()