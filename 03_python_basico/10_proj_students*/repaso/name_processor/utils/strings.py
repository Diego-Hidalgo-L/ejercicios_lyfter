
def clean_name(raw_names):
    clean_names = []
    for name in raw_names:
        clean_name = name.strip().lower()
        clean_names.append(clean_name)
    
    return clean_names

    # Utilizando "list comprehension":
    # return [name.strip().lower() for name in raw_names]


def format_name(clean_names):
    formatted_names = []
    for name in clean_names:
        formatted_name = name.capitalize()
        formatted_names.append(formatted_name)

    return formatted_names

    # Utilizando "list comprehension":
    # return [name.capitalize() for name in clean_names]