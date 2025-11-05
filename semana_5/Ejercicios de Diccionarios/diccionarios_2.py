
# Cree un programa que cree un diccionario usando dos listas del mismo tamaño.
    # Una lista para sus keys, y la otra para sus values.

list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']

my_dict = {}

for index, data_point in enumerate(list_a):
    my_dict[data_point] = list_b[index]

print(my_dict)