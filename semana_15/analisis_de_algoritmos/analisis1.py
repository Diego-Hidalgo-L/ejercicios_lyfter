
def bubble_sort(list_to_sort):
    iterations = 0 # O(1)
    swaps = 0 # O(1)
    for outer_index in range(len(list_to_sort) - 1): # O(n)
        has_made_changes = False # O(1)
        level = outer_index # O(1)
        print(f"Level: {level}") # O(1)
        for index in range(len(list_to_sort) - 1 - outer_index): # O(n) - NO O(log n), porque la cantidad de iteraciones NO se va reduciendo de manera considerable.
            current_element = list_to_sort[index] # O(1)
            next_element = list_to_sort[index + 1] # O(1)

            print(" " * level + f"--Iteración: {outer_index, index}. Elemento actual: {current_element}. Elemento siguiente: {next_element}.") # O(1)
        
            if current_element > next_element: # O(1)
                print(" " * level + f"--El elemento actual ({current_element}) es mayor que el siguiente elemento ({next_element}). Intercambiándolos.") # O(1)
                list_to_sort[index + 1] = current_element # O(1)
                list_to_sort[index] = next_element # O(1)
                has_made_changes = True # O(1)
                swaps += 1 # O(1)

        iterations += 1 # O(1)
        
        if not has_made_changes: # O(1)
            return iterations, swaps # O(1)


my_list = [19, 78, -3, 81, 34, 35, 67] # O(1)

def main():
    iterations, swaps = bubble_sort(my_list) # O(n)
    print("\n") # O(1)
    print(my_list) # O(1)
    print("Iterations:", iterations) # O(1)
    print("Swaps:", swaps) # O(1)


main() # O(n)