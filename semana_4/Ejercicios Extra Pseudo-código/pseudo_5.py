# Cree un algoritmo que le pida al usuario una velocidad en km/h y la convierta a m/s.
# Recuerde que 1 km == 1000m y 1 hora == 60 minutos * 60 segundos.

speed = int(input("Ingrese su velocidad: "))

meters_per_second = speed * 100 / (60 * 60)

print(f"Su velocidad en m/s es de: {meters_per_second}")