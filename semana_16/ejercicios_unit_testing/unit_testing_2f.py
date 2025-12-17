
def ask_for_string_input():
    my_str = input("Please enter a string of characters: ")
    return my_str


def ask_for_target_letter():
    target_letter = input("Please enter the letter you wish to count within the string: ")
    return target_letter


def count_chars(my_str, target_letter): # Function to test
    my_str = my_str.lower()
    target_letter = target_letter.lower()
    counter = 0
    for char in my_str:
        if char == target_letter:
            counter += 1
    return my_str, target_letter, counter


def main():
    my_str = ask_for_string_input()
    target_letter = ask_for_target_letter()
    counter = count_chars()
    print(f"The letter '{target_letter}' appears {counter} times in '{my_str}'.")


if __name__ == "__main__":
    main()