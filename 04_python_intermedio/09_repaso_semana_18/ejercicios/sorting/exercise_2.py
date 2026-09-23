
def reverse_bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        has_made_changes = False
        for j in range(i, 0, -1):
            current_element = my_list[j]
            previous_element = my_list[j - 1]

            if current_element < previous_element:
                my_list[j - 1] = current_element
                my_list[j] = previous_element
                has_made_changes = True
        
        if not has_made_changes:
            return


def main():
    my_list = [19, 78, -3, 81, 34, 35, 67]

    print("Before sort:")
    print(my_list)

    print("After sort:")
    reverse_bubble_sort(my_list)
    print(my_list)


main()