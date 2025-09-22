
# Cree un programa que use una lista para eliminar keys de un diccionario.

list_of_keys = ['access_level', 'age']
list_of_deleted_values = []

employee = {
    'name': 'John',
    'email': 'john@ecorp.com',
    'access_level': 5,
    'age': 28
    }

print(f"Los elementos eliminados del diccionario fueron:")

for key in list_of_keys:
    deleted_value = employee.pop(key)
    list_of_deleted_values.append(deleted_value)
    print(f"{key} : {deleted_value}")

print(f"Finalmente, el diccionario queda así: {employee}")

