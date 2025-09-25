# Pida al usuario ingresar una temperatura en Celsius.
# Conviértala a Fahrenheit y Kelvin.
# Muestre los tres valores.

celsius = float(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = celsius * (9 / 5) + 32
kelvin = celsius + 273.15

print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")
print(f"La temperatura en grados Kelvin es: {kelvin}")