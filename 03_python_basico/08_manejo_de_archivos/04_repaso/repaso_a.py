
def count_lines(filepath):
    count = 0
    with open(filepath) as file:
        for line in file.readlines():
            count += 1
    
    return count


def main():
    count = count_lines('semana_8/repaso/texto.txt')
    print(f"El texto contiene {count} líneas.")


main()