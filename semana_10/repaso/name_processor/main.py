
from utils.strings import clean_name, format_name
from utils.stats import count_letters
from utils.file_utils import save_results_in_json_file


def print_result(names_dict):
    for name, count in names_dict.items():
        print(f"{name} - {count} letters")


def main():
    raw_names = ["  JUAN", "maria ", " PEDRO ", "LuIs"]

    clean_names = clean_name(raw_names)
    formatted_names = format_name(clean_names)
    names_dict = count_letters(formatted_names)
    save_results_in_json_file(names_dict, 'semana_10/repaso/name_processor/results.json')
    print_result(names_dict)


if __name__ == "__main__":
    main()