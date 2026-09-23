
def sum_numbers(*args):
    total_sum = 0

    for arg in args: # No necesito hacer enumerate(args) cuando no voy a usar el index.
        total_sum += arg
    
    return total_sum
    # Más de Python:
    # return sum(args)


def main():
    result = sum_numbers(5, 10, 15, 20)
    print(f"La suma total es de: {result}")


main()