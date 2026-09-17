
def count_cases(text):
    lower_case = 0
    upper_case = 0

    for char in text:
        if char.islower():
            lower_case += 1
        elif char.isupper():
            upper_case += 1

    return upper_case, lower_case


def sort_hyphenated_text(text):
    split_text = text.split("-")

    for outer_index in range(len(split_text) - 1):
        has_made_changes = False

        for index in range(len(split_text) - 1 - outer_index):
            current_element = split_text[index]
            next_element = split_text[index + 1]

            if current_element > next_element:
                split_text[index] = next_element
                split_text[index + 1] = current_element

                has_made_changes = True
            
        if not has_made_changes:
            break
    
    return "-".join(split_text)


def main():
    print("\nMenu:" \
    "\n1) Count cases." \
    "\n2) Sort hyphenated text.")
    
    while True:
        try:
            option = int(input("\nPlease enter the number for the option you wish to select (1-2): "))

            if option not in (1, 2):
                print("\nError: Please enter a number between 1 and 2")
                continue

            break

        except ValueError:
            print("\nError: Please enter a number between 1 and 2")

    if option == 1:
        print("\nOption 1 selected: Count cases.")
        text = input("Enter the text: ")

        upper_case, lower_case = count_cases(text)

        print(f"\nUpper: {upper_case}")
        print(f"Lower: {lower_case}")
    
    elif option == 2:
        print("\nOption 2 selected: Sort hyphenated text.")
        text = input("Enter a list of words separated by hyphens (-): ")

        sorted_text = sort_hyphenated_text(text)

        print(f"Sorted words: {sorted_text}")


main()