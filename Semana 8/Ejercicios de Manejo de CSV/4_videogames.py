
import csv


def ask_for_rating():
    while True:
        rating = input("Ingrese la clasificación que desea buscar: ")
        rating = rating.upper()
        if rating in ("EC", "E", "E10+", "T", "M", "AO", "RP"):
            return rating
        else:
            print("\nIncorrecto. Por favor ingrese una clasificación válida.")


def read_file_and_search_rating(path, rating):
    found_any = False

    with open(path, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            value = row.get("Clasificación")
            if value == rating:
                game_title = row.get("Nombre")
                print(game_title)
                found_any = True

    if not found_any:
        print("No hay ningún título con esa clasificación.")


def main():
    rating = ask_for_rating()

    print(f"\nLos títulos que pertenecen a la clasificación '{rating}' son: ")
    read_file_and_search_rating("videogames.csv", rating)
    print("\n")


main()