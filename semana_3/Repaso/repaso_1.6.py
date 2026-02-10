
total = 6
women = 0
men = 0
counter = 1

while counter <= total:
    sex = int(input(f"Ingrese '1' si el sexo de la persona es mujer, y '2' si es hombre el sexo de la persona número {counter}: "))
    if sex == 1:
        women += 1
    elif sex == 2:
        men += 1
    else:
        print("Error. Por favor ingrese '1' o '2'.")
        continue

    counter += 1

women_percentage = (women / total) * 100
men_percentage = (men / total) * 100

print("El porcentaje de mujeres es de: ", women_percentage)
print("El porcentaje de mujeres es de: ", men_percentage)