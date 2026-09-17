
# Cree una función que le dé la vuelta a un string y lo retorne.


def invert_characters(my_string):
    inverted_string = ""
    for index in range(len(my_string) - 1, - 1, - 1):
        inverted_string += my_string[index]
    return inverted_string


def main():
    my_string = "Pizza con piña"
    inverted_string = invert_characters(my_string)
    print(inverted_string)


main()