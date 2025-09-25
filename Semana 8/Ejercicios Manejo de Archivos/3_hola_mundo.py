
def read_and_convert_to_string(path):
    with open(path, encoding="utf-8") as file:
        new_string = " ".join(file.read().splitlines())

    return new_string


def create_new_file(new_path, new_string):
    with open(new_path, 'w', encoding="utf-8") as file:
        file.write(new_string)


def main():
    new_string = read_and_convert_to_string('hola_mundo.txt')
    create_new_file('new_hola_mundo.txt', new_string)


main()