
def read_file_and_convert_to_upper_case(path):
    uppers_string = ""
    with open(path, encoding="utf-8") as file:
        line = file.read()
        uppers_string += line.upper()
    
    return uppers_string


def write_new_file(new_path, uppers_string):
    with open(new_path, 'w', encoding="utf-8") as file:
        file.write(uppers_string)


def main():
    uppers_string = read_file_and_convert_to_upper_case("hola_mundo.txt")
    write_new_file("upper_case.txt", uppers_string)


main()