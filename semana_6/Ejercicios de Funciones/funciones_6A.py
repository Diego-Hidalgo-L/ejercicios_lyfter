# Cree una función que acepte un string con palabras separadas por un guión
# y retorne un string igual pero ordenado alfabéticamente.


def convert_string_to_list(my_string):
    my_list = []
    current_word = ""
    for char in my_string:
        if (char == "-"):
            my_list.append(current_word)
            current_word = ""
        else:
            current_word += char
    my_list.append(current_word)
    return my_list


def sort_list(my_list):
    my_list.sort()
    return my_list


def convert_list_to_new_string(my_list):
    new_string = ""
    for index in range(len(my_list)):
        new_string += my_list[index]
        if index < len(my_list) - 1:
            new_string += "-"
    return new_string


def main():
    my_string = "python-variable-funcion-computadora-monitor"
    my_list = convert_string_to_list(my_string)
    my_list = sort_list(my_list)
    new_string = convert_list_to_new_string(my_list)
    print(new_string)


main()