
# Esta parte del código es por si quiero que el usuario ingrese cada string:

# def make_strings_list():
    # my_list = []
    # string_counter = 1
    # string_target = 5
    # while string_counter <= string_target:
        # my_string = input(f"Ingrese el string #{string_counter} de {string_target}: ")
        # my_list.append(my_string)
        # string_counter += 1
    # return my_list



def show_results(my_list):
    for string in my_list:
        convert_string_to_int(string)


def convert_string_to_int(string):
    try:
        string_is_int = int(string)
        print(f"'{string}' se ha convertido a: {string_is_int} ")
    except ValueError:
        print(f"No se pudo convertir el elemento: '{string}'")


def main():
    my_list = ['4', 'hola', '10', '5.2']
    print("Resultado:")
    try:
        show_results(my_list)
    except Exception as ex:
        print(ex)


main()