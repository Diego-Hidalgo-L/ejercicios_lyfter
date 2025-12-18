
# Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.


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


def make_primes_list(my_list):
    primes_list = []
    for number in my_list:
        is_prime = check_if_prime(number)
        if is_prime:
            primes_list.append(number)
    return primes_list


def main():
    my_list = [1, 4, 2, 5, 6, 7, 13, 9, 67, 104, 23, 41]
    primes_list = make_primes_list(my_list)
    print(primes_list)


main()