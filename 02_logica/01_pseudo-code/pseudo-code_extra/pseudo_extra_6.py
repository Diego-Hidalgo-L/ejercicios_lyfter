# Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas.
    # Ingrese 1 si es mujer o 2 si es hombre.
    # Muestre al final el porcentaje de mujeres y hombres.

list_of_people = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
list_length = len(list_of_people)
total_women = 0
total_men = 0

for person in list_of_people: # Como hago para que solo pueda ingresar 1 y 2?
    sex = int(input(f"Ingrese el sexo de la persona número {person}: "))
    if (sex == 1):
        total_women += 1
    elif (sex == 2):
        total_men += 1

if (total_women != 0):
    percentage_women = (total_women / list_length) * 100
    print(f"El porcentaje de mujeres es de: {percentage_women}")
else:
    print("Ninguna de las personas ingresadas es mujer")

if (total_men != 0):
    percentage_men = (total_men / list_length) * 100
    print(f"El porcentaje de hombres es de: {percentage_men}")
else:
    print("Ninguna de las personas ingresadas es hombre")