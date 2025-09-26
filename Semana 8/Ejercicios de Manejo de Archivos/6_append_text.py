
def ask_for_input():
    text = "\n" + input("Por favor ingrese el texto que desea agregar: ")
    return text


def append_text_to_file(path, text):
    with open(path, 'a', encoding="utf-8") as file:
        file.write(text)


def main():
    text = ask_for_input()
    append_text_to_file("text_for_append.txt", text)


main()