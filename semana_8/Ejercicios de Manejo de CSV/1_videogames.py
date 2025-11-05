
def input_name():
    name = input("Ingrese el nombre del videojuego: ")
    return name


def input_genre():
    genre = input("Ingrese el género del videojuego: ")
    return genre


def input_developer():
    developer = input("Ingrese el desarrollador del videojuego: ")
    return developer


def input_esrb_rating():
    esrb_rating = input("Ingrese la clasificación ESRB del videojuego: ")
    esrb_rating = esrb_rating.upper()
    return esrb_rating


def create_dict_entry(name, genre, developer, esrb_rating):
    dict_entry = {}
    
    dict_entry['Nombre'] = name
    dict_entry['Género'] = genre
    dict_entry['Desarrollador'] = developer
    dict_entry['Clasificación'] = esrb_rating
    
    return dict_entry


def input_dict_entry_to_games_list(games_list, dict_entry):
    games_list.append(dict_entry)
    print("\n¡Videojuego ingresado!")


def ask_if_go_on():
    while True:
        try:
            go_on = input("Desea ingresar otro videojuego? Sí o No: ")
            go_on = go_on.upper()

            if go_on == "SÍ" or go_on == "SI" or go_on == "NO":
                print("\n")
                return go_on
            else:
                raise ValueError
        except ValueError:
            print("Respuesta inválida. Por favor ingrese Sí o No.")


def create_games_list():
    games_list = []

    while True:
        name = input_name()
        genre = input_genre()
        developer = input_developer()
        esrb_rating = input_esrb_rating()
        dict_entry = create_dict_entry(name, genre, developer, esrb_rating)
        input_dict_entry_to_games_list(games_list, dict_entry)
        
        go_on = ask_if_go_on()
        if go_on == "NO":
            break

    return games_list


import csv


def write_csv_file(file_path, data, headers):
    with open(file_path, 'w', newline="", encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


def main():
    games_list = create_games_list()
    write_csv_file("videogames.csv", games_list, games_list[0].keys())


main()


# Grand Theft Auto IV	Accion	Rockstar Games	M
# The Elder Scrolls IV: Oblivion	RPG	Bethesda	M
# Tony Hawk's Pro Skater 2	Deportes	Activision	T