

def write_text_to_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)

text_to_write = """
Tradicionalmente, el número de especies de pingüinos a nivel mundial es de 17.
En 2006, se cambió este número a 18, cuando se empezó a reconocer al
pingüino saltarrocas como dos especies distintas:
el pingüino saltarrocas austral y el pingüino saltarrocas norteño.
"""
write_text_to_file("penguins.txt", text_to_write)