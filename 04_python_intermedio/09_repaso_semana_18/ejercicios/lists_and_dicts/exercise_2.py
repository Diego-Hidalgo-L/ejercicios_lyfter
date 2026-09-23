

def ask_for_sentence():
    return input("Please enter a sentence: ")


def reverse_sentence(my_str):
    rev_str = ""
    
    for i in range(len(my_str) -1 , -1, -1):
        rev_str += my_str[i]
    
    return rev_str


def check_if_palindrome(my_str, rev_str):
    split_str = my_str.split()
    joined_str = "".join(split_str).lower()

    split_rev = rev_str.split()
    joined_rev = "".join(split_rev).lower()

    palindrome = joined_str == joined_rev

    return palindrome, split_str


def reverse_each_word(split_str):
    rev_words = ""

    for i, word in enumerate(split_str):
        rev_word = ""

        for index in range(len(word) - 1, -1, -1):
            rev_word += word[index]
        
        if i < len(split_str) - 1:
            rev_words += rev_word + " "
        else:
            rev_words += rev_word
    
    return rev_words


def main():
    my_str = ask_for_sentence()
    rev_str = reverse_sentence(my_str)
    palindrome, split_str = check_if_palindrome(my_str, rev_str)
    rev_words = reverse_each_word(split_str)

    # Prints:
    print(f"Input: {my_str}")
    print(f"Reversed sentence: {rev_str}")
    print(f"Words reversed: {rev_words}")
    print(f"Is palindrome?", "Yes (ignoring spaces)" if palindrome else "No")


main()