
# Cree un programa que use una lista para eliminar keys de un diccionario.
    # Que pasa si tengo una lista de diccionarios?

list_of_keys = ['access_level', 'age']
# list_of_deleted_values = [] No es necesario crear una lista con esta info.

list_of_employees = [
    {
    'name': 'John',
    'email': 'john@ecorp.com',
    'access_level': 5,
    'age': 28
    },
    {
        'name': 'Jimmy',
        'email': 'jimmy@gmail.com',
        'access_level': 6,
        'age': 38
    }
]

for employee in list_of_employees:
    print(f"The eliminated data from {employee['name']}'s profile is:")
    for key in list_of_keys:
        deleted_value = employee.pop(key)
        # list_of_deleted_values.append(deleted_value) # No es necesario.
        print(f"    {key} : {deleted_value}")

print(f"In the end, the list will look like this: {list_of_employees}")
