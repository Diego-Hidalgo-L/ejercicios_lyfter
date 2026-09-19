
def sort_list(my_str, reverse):
    str_list = my_str.split(", ")
    sorted_list = sorted(str_list, reverse=reverse)
    new_str = ", ".join(sorted_list)

    return new_str


def main():
    my_str = "hola, zoológico, adiós, comer, ornitorrinco, almuerzo, postre"
    reverse = False
    new_str = sort_list(my_str, reverse)
    print(new_str)


main()