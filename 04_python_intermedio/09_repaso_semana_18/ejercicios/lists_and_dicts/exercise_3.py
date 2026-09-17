

def swap_first_and_last(my_list):
    # Edge case (eg: [] o [5]):
    if len(my_list) < 2:
        print("The list is too short. There is nothing to swap.")
        return
    else:
        first = my_list.pop(0)
        last = my_list.pop(-1)

        my_list.insert(0, last)
        my_list.append(first)

        # Alternativa:
        # my_list[0], my_list[-1] = my_list[-1], my_list[0]


def square_evens_only(my_list):
    evens_squared = []
    for n in my_list:
        if n % 2 == 0:
            evens_squared.append(n**2)
    
    return evens_squared


def calculate_running_sums(evens_squared):
    sum_list = []
    sum_track = 0

    for m in evens_squared:
        sum_track += m
        sum_list.append(sum_track)
    
    return sum_list


def main():
    my_list = [6]

    print(f"Before swap: {my_list}")
    swap = swap_first_and_last(my_list)

    if swap:
        evens_squared = square_evens_only(my_list)
        sum_list = calculate_running_sums(evens_squared)

        print(f"After swap: {my_list}")
        print(f"Evens squared: {evens_squared}")
        print(f"Running sums: {sum_list}")


main()