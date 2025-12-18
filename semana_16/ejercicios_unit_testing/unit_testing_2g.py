
def ask_for_minimum_length():
    min_len = int(input("Please enter the minimum amount of letters per word you want: "))
    return min_len


def return_new_list(my_list, min_len): # Function to test
    new_list = []

    if not my_list:
        return "The list is empty."
    else:
        for word in my_list:
            if len(word) >= min_len:
                new_list.append(word)
    if not new_list:
        return (f"There are no words with a minimum length of {min_len} letters in the list you entered.")
    else:
        return new_list


def main():
    my_list = ["cielo", "sol", "maravilloso", "día"]
    min_len = ask_for_minimum_length()
    new_list = return_new_list(my_list, min_len)
    print(new_list)


if __name__ == "__main__":
    main()