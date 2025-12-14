
def sort_string(my_str):
    if not isinstance(my_str, str):
        raise AttributeError("The input must be a string.")
    elif my_str == "":
        return "The string is empty."
    else:
        my_list = my_str.split("-")
        my_list.sort()
        new_str = "-".join(my_list)
        return new_str
