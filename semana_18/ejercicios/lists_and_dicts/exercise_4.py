

def build_numbers_list():
    my_list = []
    maximum = None
    minimum = None
    counter = 1

    while counter <= 10:
        try:
            n = int(input(f"Please enter number {counter}: "))
        except ValueError:
            print("Enter a valid integer")
            continue
        
        if maximum is None or n > maximum:
            maximum = n

        if minimum is None or n < minimum:
            minimum = n

        my_list.append(n)
        counter += 1
    
    return my_list, maximum, minimum


def calculate_average(my_list):
    return round(sum(my_list) / len(my_list), 2)


def determine_above_average_count(my_list, avg, maximum):
    above_avg = 0
    max_index = None

    for i, n in enumerate(my_list):
        if n > avg:
            above_avg += 1
        
        if n == maximum:
            max_index = i
    
    return above_avg, max_index


def main():
    my_list, maximum, minimum = build_numbers_list()
    avg = calculate_average(my_list)
    above_avg, max_index = determine_above_average_count(my_list, avg, maximum)

    # Prints:
    print(f"Full list: {my_list}")
    print(f"Maximum number: {maximum}")
    print(f"Minimum number: {minimum}")
    print(f"Average: {avg}")
    print(f"How many above the average: {above_avg}")
    print(f"Index of the maximum value: {max_index}")


main()