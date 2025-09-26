
import csv


def ask_for_developer():
    developer = input("Ingrese el desarrollador que desea buscar: ")
    return developer


def read_file_and_search_developer(path, developer):
    found_dev = False

    with open(path, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            value = row.get("Desarrollador")
            if value == developer:
                game_title = row.get("Nombre")
                game_genre = row.get("Género")
                game_rating = row.get("Clasificación")
                print(f" - {game_title} (Clasificación: {game_rating}, Género: {game_genre})")
                found_dev = True
            
    if not found_dev:
        print(f"No se encontró ningún videjuego desarrolado por {developer}.")


def main():
    developer = ask_for_developer()

    print(f"\nVideojuegos desarrollados por {developer}: ")
    read_file_and_search_developer("videogames.csv", developer)
    print("\n")


main()