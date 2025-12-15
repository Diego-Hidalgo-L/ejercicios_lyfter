
def count_chars():
    my_str = str(input("Please enter a string of characters: ")).lower()
    target_letter = str(input("Please enter the letter you wish to count within the string: ")).lower()
    counter = 0
    for char in my_str:
        if char == target_letter:
            counter += 1
    return my_str, target_letter, counter


def main():
    my_str, target_letter, counter = count_chars()
    print(f"The letter '{target_letter}' appears {counter} times in '{my_str}'.")


main()