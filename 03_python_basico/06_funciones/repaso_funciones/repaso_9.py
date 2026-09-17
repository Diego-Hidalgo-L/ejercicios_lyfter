
def return_multiple_values(my_list):
    big_num = my_list[0]
    small_num = my_list[0]
    total_sum = 0

    for n in my_list:
        if n > big_num:
            big_num = n
        if n < small_num:
            small_num = n
        total_sum += n
    
    avg = total_sum / len(my_list)

    return big_num, small_num, avg


def main():
    my_list = [45, 76, 89, 123, 12, 453, 999]
    big_num, small_num, avg = return_multiple_values(my_list)
    print("El número mayor es:", big_num)
    print("El número menor es:", small_num)
    print("El promedio es:", avg)


main()