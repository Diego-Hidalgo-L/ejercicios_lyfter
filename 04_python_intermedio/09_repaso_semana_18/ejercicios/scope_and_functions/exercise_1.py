
def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        divisor = 3
        limit = int(number ** 0.5)
        while divisor <= limit:
            if number % divisor == 0:
                return False
            divisor += 2

        return True


def get_primes(my_list):
    primes_list = []

    for number in my_list:
        if is_prime(number):
            primes_list.append(number)
    
    return primes_list


def calculate_gaps(primes_list):
    gaps_list = []

    for index in range(len(primes_list) - 1):
        gap = abs(primes_list[index + 1] - primes_list[index])
        gaps_list.append(gap)
    
    return gaps_list


def main():
    my_list = [1, 2, 3, 4, 13, 15, 17, 19, 20, 97, 100, 101]

    primes_list = get_primes(my_list)
    gaps_list = calculate_gaps(primes_list)

    # Prints:
    print(f"Original list: {my_list}")
    print(f"Primes: {primes_list}")
    print(f"Gaps: {gaps_list}")


main()