
def elevate_second_power(num):
    num_elev = num ** 2
    
    return num_elev


def iterate_list(my_list):
    new_list = []

    for num in my_list:
        num_elev = elevate_second_power(num)
        new_list.append(num_elev)
    
    return new_list


def main():
    my_list = [45, 76, 89, 123, 12, 453, 999]
    new_list = iterate_list(my_list)
    print(new_list)


main()
