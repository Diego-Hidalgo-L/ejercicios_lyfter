
def read_file_and_count_words(path):
    with open(path, encoding="utf-8") as file:
        words = file.readlines()            # read the entire file as one string      # split on whitespace into a list of words
        word_count = len(words)            # count how many items in the list
    
    return word_count

def main():
    word_count = read_file_and_count_words("hola_mundo.txt")
    print(f"Este archivo contiene {word_count} palabras")


main()