
def bubble_sort(my_list):
    for outer_index in range(len(my_list) - 1):
        has_made_changes = False
        for index in range(len(my_list) - 1 - outer_index):
            current_element = my_list[index]
            next_element = my_list[index + 1]

            if current_element > next_element:
                my_list[index + 1] = current_element
                my_list[index] = next_element
                has_made_changes = True

        if not has_made_changes:
            return


def main():
    my_list = [19, 78, -3, 81, 34, 35, 67]

    print("Before sort:")
    print(my_list)

    print("After sort:")
    bubble_sort(my_list)
    print(my_list)


main()