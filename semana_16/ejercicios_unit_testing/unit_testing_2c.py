
def count_letters_per_case(my_str):
    upper_case = 0
    lower_case = 0

    if not isinstance(my_str, str):
        raise TypeError("Error: The input must be a string.")
    for char in my_str:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
    
    return upper_case, lower_case