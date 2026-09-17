
def bubble_sort(my_list):
    iterations = 0
    swaps = 0
    for outer_index in range(len(my_list) - 1):
        has_made_changes = False
        for index in range(len(my_list) - 1 - outer_index):
            current_number = my_list[index]
            next_number = my_list[index + 1]

            if current_number > next_number:
                my_list[index] = next_number
                my_list[index + 1] = current_number
                has_made_changes = True
                swaps += 1
        
        iterations += 1
            
        if not has_made_changes:
            return iterations, swaps

def validate_list(my_list):
    try:
        for num in my_list:
            if isinstance(num, int):
                continue
            else:
                raise ValueError(f"\nValueError: '{num}' es un valor no numérico.")
        return bubble_sort(my_list)
    except ValueError as e:
        print(e)


my_list = [76, 21, 'hola', 99, 15, 34]

def main():
    try:
        iterations, swaps = validate_list(my_list)
        print("\n")
        print(my_list)
        print("Iterations:", iterations)
        print("Swaps:", swaps)
    except TypeError:
        print("TypeError: La lista contiene valores no numéricos.")


main()