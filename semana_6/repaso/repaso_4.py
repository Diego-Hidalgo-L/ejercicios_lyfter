

# Mi versión original con correcciones:
def revert_chars_per_word(my_str):
    words = my_str.split()
    inverted = ""
    
    for index in range(len(words)):
        word = words[index]
        for i in range(len(word) - 1, -1, -1):
            inverted += word[i]
        if index < len(words) - 1:
            inverted += " "
    
    return inverted


# Versión más elegante:
def revert_chars(my_str):
    words = my_str.split()
    result = []

    for word in words:
        inverted_word = ""

        for i in range(len(word) - 1, -1, -1):
            inverted_word += word[i]

        result.append(inverted_word)

    return " ".join(result)


def main():
    my_str = "Hola mundo cruel"
    inverted = revert_chars(my_str)
    print(inverted)


main()