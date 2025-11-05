
def run_through_my_list(my_list):
    floats_list = []
    for string in my_list:
        convert_string_to_float(string, floats_list)
    return floats_list


def convert_string_to_float(string, floats_list):
    string_is_float = 0
    try:
        string_is_float += float(string)
        floats_list.append(string_is_float)
        print(f"{string_is_float}, sumado correctamente")
    except ValueError:
        print(f"Elemento inválido: {string}")


def sum_values(floats_list):
    total_sum = 0
    for number in floats_list:
        total_sum += number
    return total_sum


def main():
    my_list = ['10', 'manzana', '5.5', '3', 'n/a']
    try:
        floats_list = run_through_my_list(my_list)
        total_sum = sum_values(floats_list)
        print(f"La suma total es de: {total_sum}")
    except Exception as ex:
        print(ex)


main()
