# Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.


# string + string
string_1 = "Hola"
string_2 = " mundo!"
result = string_1 + string_2
print(result)
# FUNCIONA: "Hola mundo!"


# string + int
# string_1 = "Tengo "
# integer = 28
# string_2 = " años"
# result = string_1 + integer + string_2
# print(result)
# TypeError: can only concatenate str (not "int") to str.
# Necesitaría usar alguna forma de concatenación (como usar un F string) para concatenar el int al string.


# int + string
# integer = 2025
# string = ", es el año en el que estamos"
# result = integer + string
# print(result)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'.
# Para corregir esto necesito cambiar el int a str, i.e.: str(integer)


# list + list
list_1 = ['Sabbath', 'Bloody', 'Sabbath']
list_2 = [6, 6, 6]
result = list_1 + list_2
print(result)
# FUNCIONA: ['Sabbath', 'Bloody', 'Sabbath', 6, 6, 6]
# Ambas listas se concatenan y crean una nueva lista (result).
# No importa que ambas listas estén compuestas de tipos de elementos diferentes.


# string + list
string = "Me gusta la canción "
list_1 = ['Sabbath', 'Bloody', 'Sabbath']
result = string + str(list_1)
print(result)
# TypeError: can only concatenate str (not "list") to str.
# Siempre que tengo un string primero en alguna suma, el programa entiende que los estoy tratando de concatenar.
# De nuevo, la forma de arreglar esto es convirtiendo el elemento a str: result = string + str(list_1)

    # Esta es una forma de lograr lo mismo pero agregando cada index de list_1 al string original, como uno solo.
for index in range(len(list_1)):
    string += list_1[index] + " "
print(string)


# list + string
list_1 = ['Sabbath', 'Bloody', 'Sabbath']
string = "Me gusta la canción "

# result = list_1 + string 
# print(result)     # Tira error.

# result = list_1 + list(string) 
# print(result)     # Agrega cada letra del string a la lista en un índice separado.

list_1.insert(0, string) # Esta es la forma más correcta.
print(list_1)


# float + int
my_float = 3.14
my_int = 123
result = my_float + my_int
print(result)
# FUNCIONA: Suma los dos valores.


# bool + bool
var_1 = True
var_2 = False
result = var_1 + var_1 + var_1 + var_2
print(result)
# True = 1; False = 0
# Se suman los valores de cada uno como si fueran integers.