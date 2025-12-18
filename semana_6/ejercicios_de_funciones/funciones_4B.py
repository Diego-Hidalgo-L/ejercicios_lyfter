
# Cree una función que le dé la vuelta a un string y lo retorne.


def invert_characters(my_string):
    for index in range(len(my_string) - 1, - 1, - 1):
        char = my_string[index]
        print(char)


def main():
    my_string = "Pizza con piña"
    invert_characters(my_string)


main()