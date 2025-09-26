
import json


def read_file_and_list_poke_types(file_path):  # Hacemos NUEVO diccionario de una vez?
    my_poke_types_list = []

    with open(file_path, 'r', encoding='utf-8') as file:
        my_poke_list = json.load(file)

        for entry in my_poke_list:
            poke_type = entry.get('type')
            for ind_type in poke_type:
                if ind_type not in my_poke_types_list:
                    my_poke_types_list.append(ind_type)
                else:
                    continue
    
    return my_poke_list, my_poke_types_list


def create_dict_per_types(my_poke_list, my_poke_types_list):
    dict_per_poke_types = {}

    for poke_type in my_poke_types_list:
        dict_per_poke_types[poke_type] = []
        for entry in my_poke_list:
            my_poke_name_english = entry.get('name', {}).get('english')
            my_poke_lvl = entry.get('lvl')
            my_poke_type = entry.get('type', [])

            if poke_type in my_poke_type:
                dict_per_poke_types[poke_type].append({
                    'name_english' : my_poke_name_english,
                    'lvl' : my_poke_lvl
                })

    return dict_per_poke_types


def calculate_lvl_avg(dict_per_poke_types):
    dict_per_lvl_avg = {}
    for poke_type, values in dict_per_poke_types.items():
        lvl_sum = 0
        for pokemon in values:
            poke_lvl = pokemon.get('lvl')
            lvl_sum += poke_lvl
            lvl_avg = lvl_sum / len(values)
        dict_per_lvl_avg[poke_type] = f'{lvl_avg}'

    return dict_per_lvl_avg


def iterate_dict_per_lvl_avg(dict_per_lvl_avg):
    for poke_type, lvl_avg in dict_per_lvl_avg.items():
        print(f"Type: {poke_type} --> Level average: {lvl_avg}")


def main():
    (my_poke_list,  my_poke_types_list) = read_file_and_list_poke_types("pokemon_list.json")
    dict_per_poke_types = create_dict_per_types(my_poke_list,  my_poke_types_list)
    dict_per_lvl_avg = calculate_lvl_avg(dict_per_poke_types)
    iterate_dict_per_lvl_avg(dict_per_lvl_avg)


main()


dict_per_poke_types = {
'Electric': [
    {
        'name_english': 'Pikachu',
        'lvl': 45
        }
        ],
'Fire': [
    {
        'name_english': 'Charmander',
        'lvl': 32
        },
        {
        'name_english': 'Entei',
        'lvl': 67
        }
        ],
'Water': [
    {
        'name_english': 'Squirtle',
        'lvl': 28
        }
        ],
'Dragon': [
    {
        'name_english': 'Rayquaza',
        'lvl': 88
        },
        {'name_english': 'Latias',
        'lvl': 72
        }
        ],
'Flying': [
    {
        'name_english': 'Rayquaza',
        'lvl': 88
        }
        ],
'Psychic': [
    {
        'name_english': 'Mewtwo',
        'lvl': 95
        },
        {
        'name_english': 'Latias',
        'lvl': 72
        }
        ],
'Ghost': [
    {
        'name_english': 'Gengar',
        'lvl': 81
        }
        ],
'Poison': [
    {
        'name_english': 'Gengar',
        'lvl': 81
        }
        ],
'Fighting': [
    {
        'name_english': 'Machamp',
        'lvl': 54
        }
        ],
'Rock': [
    {
        'name_english': 'Onix',
        'lvl': 39
        }
        ],
'Ground': [
    {'name_english': 'Onix',
    'lvl': 39}
    ]
}