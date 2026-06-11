

def show_menu():
    while True:
        print("\nMenu:" \
        "\n1) Add." \
        "\n2) Subtract." \
        "\n3) Multiply." \
        "\n4) Divide." \
        "\n5) Clear." \
        "\n6) Quit.")

        try:
            option = int(input("Please select an option: "))

            if option not in range(1, 7):
                raise ValueError("Please enter only integers between 1-6")

            return option

        except ValueError as e:
            print(f"{type(e).__name__}: {e}")


def validate_number(prompt):
    while True:
        try:
            return float(input(prompt))
        
        except ValueError:
            print("Error: Please enter a valid number")


def add(starting_number, history):
    new_number = validate_number("Enter a number to add: ")
    result = starting_number + new_number
    history.append(f"{starting_number} + {new_number} = {result}")

    return result


def subtract(starting_number, history):
    new_number = validate_number("Enter a number to subtract: ")
    result = starting_number - new_number
    history.append(f"{starting_number} - {new_number} = {result}")

    return result


def multiply(starting_number, history):
    new_number = validate_number("Enter a number to multiply: ")
    result = starting_number * new_number
    history.append(f"{starting_number} x {new_number} = {result}")

    return result


def divide(starting_number, history):
    while True:
        new_number = validate_number("Enter a number to divide: ")

        if new_number == 0:
            print("Error: Cannot divide by zero")
            continue

        result = starting_number / new_number
        history.append(f"{starting_number} / {new_number} = {result}")

        return result



def clear(history):
    history.append("CLEAR -> 0")
    return 0


def main():
    starting_number = 0.0
    history = []

    while True:
        option = show_menu()

        if option == 1:
            print("\nOption 1 selected:")
            starting_number, history = add(starting_number, history)
            print(f"Result: {starting_number}")
        elif option == 2:
            print("\nOption 2 selected:")
            starting_number, history = subtract(starting_number, history)
            print(f"Result: {starting_number}")
        elif option == 3:
            print("\nOption 3 selected:")
            starting_number, history = multiply(starting_number, history)
            print(f"Result: {starting_number}")
        elif option == 4:
            print("\nOption 4 selected:")
            starting_number, history = divide(starting_number, history)
            print(f"Result: {starting_number}")
        elif option == 5:
            print("\nOption 5 selected:")
            starting_number = clear()
            print(f"Result: {starting_number}")
        else:
            print("\nOption 6 selected:")
            print("Quit program.")

            for item in history:
                print(item)

            return
    
        if abs(starting_number) > 1_000_000:
                print("Warning: 1,000,000 exceeded.")


main()