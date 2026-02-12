
def change_list(my_list):
    new_list = []

    for word in my_list:
        if len(word) > 4 and word[0].lower() in "aeiouáéíóú":
            new_list.append(word)

    return new_list


def main():
    my_list = ['hola', 'zoológico', 'ola', 'adiós', 'comer', 'ornitorrinco', 'almuerzo', 'postre']
    new_list = change_list(my_list)
    print(new_list)


main()