# Cree un pseudocódigo que le pida un tiempo en segundos al usuario.
# Calcule si es menor o mayor a 10 minutos.
    # Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos.
    # Si es mayor, muestre “Mayor”.
    # Si es exactamente igual, muestre “Igual”.

time_in_seconds = int(input("Ingrese su tiempo final en segundos: "))

if (time_in_seconds < 600):
    spare_time = 600 - time_in_seconds
    print(f"Faltan {spare_time} segundos para llegar a los 10 minutos")
elif (time_in_seconds > 600):
    print("Mayor")
else:
    print("Igual")