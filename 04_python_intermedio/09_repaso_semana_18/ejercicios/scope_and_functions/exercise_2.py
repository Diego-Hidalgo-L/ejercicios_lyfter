
def count_char_occurrences():
    while True:
        word = input("Please enter a word: ").strip().lower()

        if not word.isalpha():
            print("Error: Please enter only words, not numbers or different characters")
            continue

        if not word:
            print("Error: The word cannot be empty")
            continue

        target = input("Now enter the letter you wish to count within the given word: ").strip().lower()

        if len(target) != 1 or not target.isalpha():
            print("Error: Please enter exactly one (1) alphabetical letter")
            continue

        break
    
    print(f"The letter '{target}' appears {word.count(target)} times in the word '{word}'.")


def count_vowels():
    vowels = 'aeiou'

    while True:
        text = input("Please enter a text: ")
        my_text = text.lower()

        if not text:
            print("Error: The text cannot be empty")
            continue
        
        break

    vowel_count = 0

    for char in my_text:
        if char in vowels:
            vowel_count += 1

    print(f"There are {vowel_count} vowel(s) in the text '{text}'")


def reverse_words_alphabetically():
    my_str = input("\nPlease input a series of words separated by hyphens (-): ")
    my_list = my_str.split("-")
    my_list.sort()
    rev_str = ""

    for index in range(len(my_list) -1, -1, -1):
        if index == len(my_str) - 1:
            rev_str += my_list[index]
        else:
            rev_str += my_list[index] + "-"
    
    print(f"\nReversed input: {rev_str}")


def word_frequency():
    text = input("\nPlease enter the text you wish to count: ")
    split_text = text.split()
    word_dict = {}

    for word in split_text:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    
    print("\nResults:")
    print(word_dict)


def main():
    print("\nMenu:" \
    "\n1) Count how many times a selected letter appears in a word." \
    "\n2) Count how many vowels appear in a text" \
    "\n3) Reverse words alphabetically." \
    "\n4) Count how many times a selected word appears in a text.")

    while True:
        try:
            option = int(input("\nPlease enter the number for the option you wish to select (1-4): "))

            if option not in (1, 2, 3, 4):
                print("\nError: Please enter a number between 1 and 4")
                continue
            break

        except ValueError:
            print("\nError: Please enter a number between 1 and 4")

    if option == 1:
        print("\nOption 1 selected: Count letter occurrences in a word")
        count_char_occurrences()
    elif option == 2:
        print("\nOption 2 selected: Count vowels in a text")
        count_vowels()
    elif option == 3:
        print("\nOption 3 selected: Reverse words alphabetically")
        reverse_words_alphabetically()
    elif option == 4:
        print("\nOption 4 selected: Count word occurrences in a text")
        word_frequency()


main()