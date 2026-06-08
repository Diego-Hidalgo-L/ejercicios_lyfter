
import random

secret = random.randint(1, 100)
attempts = 7
best_guess = 0

while attempts > 0:
    try:
        guess = int(input("\nGuess a number between 1 and 100: "))
    except ValueError:
        print("Please enter a valid integer")
        continue

    if not 1 <= guess <= 100:
        print("Number must be between 1 and 100")
        continue

    if guess == secret:
        print(f"\nCorrect! The secret number was: {secret}\n")
        break

    if best_guess is None or abs(secret - guess) < abs(secret - best_guess):
        best_guess = guess

    attempts -= 1

    if guess > secret:
        print(f"Too high! Attempts left: {attempts}")
    elif guess < secret:
        print(f"Too low! Attempts left: {attempts}")


if attempts == 0:
    print(f"\nGame over! The number was: {secret}. Your best guess was: {best_guess}.\n")