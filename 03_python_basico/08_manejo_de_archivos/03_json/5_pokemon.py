
import json


def read_json_file_and_print_info(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        pokemon_list = json.load(file)

        for entry in pokemon_list:
            name_english = entry.get('name', {}).get('english')
            print(f"Nombre: {name_english}")
            
            attack = entry.get('base', {}).get('Attack')
            print(f"Ataque: {attack}")

            defense = entry.get('base', {}).get('Defense')
            print(f"Defensa: {defense}")

            speed = entry.get('base', {}).get('Speed')
            print(f"Velocidad: {speed}")

            print("---------------")


def main():
    read_json_file_and_print_info("pokemon_list.json")


main()