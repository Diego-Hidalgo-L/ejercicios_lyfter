
def reverse_bubble_sort(my_list):
    level = 0
    for outer_index in range(len(my_list) - 1, - 1, - 1):
        has_made_changes = False
        print(" " * level + f"Level: {level}")
        for index in range(len(my_list) - 1, -1 + level, -1):
            current_number = my_list[index]
            prev_number = my_list[index - 1]

            if index == 0:
                prev_number = None
                print(" " * level + f"--Index: {outer_index, index} - Current number: {current_number} - Previous number: {prev_number}.")
                break

            print(" " * level + f"--Index: {outer_index, index} - Current number: {current_number} - Previous number: {prev_number}.")

            if current_number < prev_number:
                print(" " * level + f"** {current_number} is less than {prev_number}. Switching places...")
                my_list[index] = prev_number
                my_list[index - 1] = current_number
                has_made_changes = True
            else:
                print(" " * level + "--No changes made.")
        
        level += 1

        if not has_made_changes:
            return




my_list = [19, 78, -3, 81, 34, 35, 67]

reverse_bubble_sort(my_list)

print(my_list)