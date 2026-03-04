
import json

def read_poke_list(path):
    with open(path, 'r') as file:
        poke_list = json.load(file)
    
    return poke_list


def append_new_pokemon(poke_list, new_pokemon):
    poke_list.append(new_pokemon)
    
    return poke_list


def overwrite_poke_list(path, data):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    new_pokemon = {
        "name": {
            "english": "Bulbasaur"
        },
        "type": [
            "Grass"
        ],
        "base": {
            "HP": 35,
            "Attack": 55,
            "Defense": 40,
            "Sp. Attack": 50,
            "Sp. Defense": 50,
            "Speed": 90
        }
    }

    poke_list = read_poke_list('semana_8/repaso/pokemons.json')
    poke_list = append_new_pokemon(poke_list, new_pokemon)
    overwrite_poke_list('semana_8/repaso/pokemons.json', poke_list)


main()