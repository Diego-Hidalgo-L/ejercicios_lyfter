
def bubble_sort(list_to_sort):
    for outer_index in range(len(list_to_sort) - 1):
        level = outer_index
        has_made_changes = False
        for index in range(0, len(list_to_sort) - 1 - outer_index):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index + 1]
    
            print(" " * level + f"-- Iteración: {outer_index, index}. Elemento actual: {current_element}. Siguiente elemento: {next_element}.")

            if current_element > next_element:
                print(f"El elemento actual ({current_element}) es mayor que el elemento siguiente ({next_element}). Intercambiándolos...")
                list_to_sort[index] = next_element
                list_to_sort[index + 1] = current_element
                has_made_changes = True
        if not has_made_changes:
            return


my_test_list = [1, 2, 3, 10, 4, 5, 6, 7, 8]

bubble_sort(my_test_list)

print(my_test_list)