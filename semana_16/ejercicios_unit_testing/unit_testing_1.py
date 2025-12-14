
def bubble_sort(list_to_sort):
    iterations = 0 
    swaps = 0

    if list_to_sort == []:
        return None, None
    elif not isinstance(list_to_sort, list):
        raise ValueError("You must enter a list of integers.")
    
    for outer_index in range(len(list_to_sort) - 1): 
        has_made_changes = False
        level = outer_index 
        print(f"Level: {level}")
        for index in range(len(list_to_sort) - 1 - outer_index):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index + 1]

            print(" " * level + f"--Iteración: {outer_index, index}. Elemento actual: {current_element}. Elemento siguiente: {next_element}.")
        
            if current_element > next_element:
                print(" " * level + f"--El elemento actual ({current_element}) es mayor que el siguiente elemento ({next_element}). Intercambiándolos.")
                list_to_sort[index + 1] = current_element
                list_to_sort[index] = next_element
                has_made_changes = True
                swaps += 1

        iterations += 1
        
        if not has_made_changes:
            return iterations, swaps

# my_list = []

# my_list = [19, 78, -3, 81, 34, 35, 67]

# my_list = [59, 9, 71, 94, 21, 26, 80, 68, 83, 13, 27, 7, 4, 53, 84, 38, 51, 69, 7, 68, 31, 20, 84, 67, 27, 9, 48, 61, 98, 85, 99, 32, 97, 50, 50, 99, 87, 41, 96, 51, 89, 52, 98, 11, 31, 67, 19, 91, 5, 95, 57, 58, 62, 13, 2, 51, 44, 90, 12, 43, 29, 88, 66, 21, 4, 40, 35, 48, 68, 62, 10, 21, 99, 12, 19, 91, 61, 26, 18, 48, 1, 29, 92, 59, 62, 79, 96, 66, 69, 15, 18, 93, 9, 2, 36, 69, 3, 98, 10, 38, 86]

# def main():
#     iterations, swaps = bubble_sort(my_list)
#     print("\n")
#     print(my_list)
#     print("Iterations:", iterations)
#     print("Swaps:", swaps)


# main()