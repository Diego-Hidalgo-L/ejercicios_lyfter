
my_num = int(input("Ingrese un número: "))

if my_num % 3 == 0 and my_num % 5 == 0:
    print("FizzBuzz")
elif my_num % 3 == 0:
    print("Fizz")
elif my_num % 5 == 0:
    print("Buzz")
else:
    print("El número no es divisible entre 3 ni 5.")