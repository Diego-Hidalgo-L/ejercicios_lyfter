
def return_total_product(my_list):
    product = 1

    for n in my_list:
        product *= n

    return product


def main():
    my_list = [2, 3, 4]
    product = return_total_product(my_list)
    print("El producto total es de:", product)


main()