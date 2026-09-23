

# 3. Cree un programa con un número secreto del 1 al 10.
    # El programa no debe cerrarse hasta que el usuario adivine el número.
    # Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.


new_number = 0
loop_ender = 0
import random

while (loop_ender != 1): 
    secret_number = random.randint(1, 10)
    print(secret_number)

    while (new_number != secret_number):
        new_number = int(input("Guess a number from 1 to 10: "))
        if (new_number == secret_number):
            print("Correct!")
            loop_ender += 1
        elif (new_number != secret_number):
            print("Wrong! Try again.")

