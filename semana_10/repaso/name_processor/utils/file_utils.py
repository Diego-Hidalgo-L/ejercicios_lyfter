
import json

def save_results_in_json_file(names_dict, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(names_dict, file, indent=4, ensure_ascii=False)
