
def count_vowels():
    my_str = input("Please enter a string of characters: ")
    counter = 0
    for char in my_str:
        if char in "aeiou":
            counter += 1
    return counter


def main():
    counter = count_vowels()
    print(f"There are {counter} vowels in the string.")


main()