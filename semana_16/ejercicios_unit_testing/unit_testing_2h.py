
def ask_for_string():
    my_str = input("Please enter a string of characters: ")
    return my_str


def count_vowels(my_str): # Function to test
    my_str = my_str.lower()
    counter = 0
    for char in my_str:
        if char in "aeiou":
            counter += 1
    return counter


def main():
    my_str = ask_for_string()
    counter = count_vowels(my_str)
    print(f"There are {counter} vowels in the string: '{my_str}'.")


if __name__ == "__main__":
    main()