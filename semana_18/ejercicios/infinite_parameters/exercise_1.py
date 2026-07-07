
def get_sum(numbers):
    total_sum = 0

    for arg in numbers:
        total_sum += arg
    
    return total_sum


def get_average(numbers, round_num):
    total = get_sum(numbers)
    avg = total / len(numbers)

    if round_num is not None:
        return round(avg, round_num)
    
    return avg


def get_min(numbers):
    min_num = None

    for arg in numbers:
        if min_num is None or arg < min_num:
            min_num = arg
    
    return min_num


def get_max(numbers):
    max_num = None

    for arg in numbers:
        if max_num is None or arg > max_num:
            max_num = arg
    
    return max_num


def stats(*numbers, **options):
    result = {}

    round_num = options.get('round_to')

    if options.get('include_sum', False):
        result['sum'] = get_sum(numbers)
    
    if options.get('include_average', False):
        result['average'] = get_average(numbers, round_num)
    
    if options.get('include_min', False):
        result['min'] = get_min(numbers)

    if options.get('include_max', False):
        result['max'] = get_max(numbers)

    return result


def main():
    print(stats(4, 7, 2, 9, 1, include_sum=True, include_average=True, round_to=1))
    print(stats(10, 5, 8, include_min=True, include_max=True))


main()