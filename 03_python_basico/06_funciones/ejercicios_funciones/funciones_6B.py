# Cree una función que acepte un string con palabras separadas por un guión
# y retorne un string igual pero ordenado alfabéticamente.



def convert_string_to_list(my_string):
    my_list = my_string.split("-")
    return my_list


def sort_list(my_list):
    sorted_list = sorted(my_list)
    return sorted_list


def convert_list_to_new_string(sorted_list):
    new_string = ""
    for index in range(len(sorted_list)):
        new_string += sorted_list[index]
        if index < len(sorted_list) - 1:
            new_string += "-"
    return new_string


def main():
    my_string = "python-variable-funcion-computadora-monitor"
    my_list = convert_string_to_list(my_string)
    sorted_list = sort_list(my_list)
    new_string = convert_list_to_new_string(sorted_list)
    print(new_string)


main()