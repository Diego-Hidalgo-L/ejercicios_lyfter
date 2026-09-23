
def sum_ints(my_list):
    total = 0

    #Mi versión original:
    # for num in my_list:
    #     if isinstance(num, bool):
    #         continue
    #     elif isinstance(num, (int, float)):
    #         total += num


    # Versión más profesional:
    for num in my_list:
        if isinstance(num, (int, float)) and not isinstance(num, bool):
            total += num

    return total


def main():
    my_list = [4, "a", 10, True, 6]
    total_sum = sum_ints(my_list)
    print(total_sum)


main()