
def check_if_prime(number):
    if number < 2:
        is_prime = False
    elif number == 2:
        is_prime = True
    elif number % 2 == 0:
        is_prime = False
    else:
        divisor = 3
        is_prime = True
        while divisor <= number ** 0.5:
            if number % divisor == 0:
                is_prime = False
                break
            divisor += 2

    return is_prime


def make_primes_dict(my_list):
    primes_dict = {
        "primos": [],
        "no primos": []
        }

    for number in my_list:
        is_prime = check_if_prime(number)
        if is_prime:
            primes_dict.get("primos").append(number)
        else:
            primes_dict.get("no primos").append(number)

    return primes_dict


def main():
    my_list = [1, 4, 2, 5, 6, 7, 13, 9, 67, 104, 23, 41]
    primes_dict = make_primes_dict(my_list)
    print(primes_dict)


main()