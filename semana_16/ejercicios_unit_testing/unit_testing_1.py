
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

my_list = []

my_list = [19, 78, -3, 81, 34, 35, 67]

def main():
    iterations, swaps = bubble_sort(my_list)
    print("\n")
    print(my_list)
    print("Iterations:", iterations)
    print("Swaps:", swaps)

if __name__ == "__main__":
    main()