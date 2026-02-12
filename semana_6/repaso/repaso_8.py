
my_list = []

def add_elements_to_list(my_list):
    new_elements = [1, 2, 3, 4, 5]
    my_list.extend(new_elements)

    return my_list


def reassign_list(my_list):
    my_list = [6, 7, 8, 9, 10]

    return my_list


print(add_elements_to_list(my_list))
print(reassign_list(my_list))
print(my_list)