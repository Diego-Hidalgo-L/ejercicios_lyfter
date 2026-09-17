
def count_letters(cap_names):
    names_dict = {}
    
    for name in cap_names:
        names_dict[name] = len(name)
    
    return names_dict