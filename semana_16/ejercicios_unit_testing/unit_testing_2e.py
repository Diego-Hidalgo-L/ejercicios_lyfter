
def check_if_prime(number):
    if isinstance(number, int):
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
    else:
        raise TypeError("The input must be an integer or a float.")


def make_primes_list(my_list):
    primes_list = []
    if not isinstance(my_list, list):
        raise TypeError("The input must be a list of integers.")
    elif not my_list:
        return "The list is empty."
    else:
        for number in my_list:
            is_prime = check_if_prime(number)
            if is_prime:
                primes_list.append(number)
    return primes_list