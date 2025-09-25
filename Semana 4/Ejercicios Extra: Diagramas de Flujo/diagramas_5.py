# Cree un diagrama de flujo que le pida un numero al usuario.
    # Muestre “Fizz” si es divisible entre 3.
    # Muestre “Buzz” si es divisible entre 5.
    # Muestre “FizzBuzz” si es divisible entre ambos.

number = int(input("Ingrese un número: "))

if ((number % 3 == 0) & (number % 5 == 0)):
    print("FizzBuzz")
elif (number % 3 == 0):
    print("Fizz")
elif (number % 5 == 0):
    print("Buzz")