
def sum_all_elements(my_list):
    total_sum = 0
    for element in my_list:
        if not isinstance(element, int):
            raise ValueError("All elements must be integers.")
        total_sum += element
    return total_sum

