
def invert_string(my_str):
    inverted_str = ""
    
    if not isinstance(my_str, str):
        raise TypeError("Error: The input must be a string of characters.")
    else:
        for index in range(len(my_str) - 1, -1, -1):
            inverted_str += my_str[index]

    if inverted_str == "":
        return "The string is empty."
    else:
        return inverted_str

