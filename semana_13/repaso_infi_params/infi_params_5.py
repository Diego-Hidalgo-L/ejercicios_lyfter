
def calculate_average(*numbers, round_result):
    if not numbers:
        return None

    avg = sum(numbers) / len(numbers)
    
    if round_result:
        return round(avg, 2)

    return avg


def main():
    result = calculate_average(10, 20, 30, 43, round_result=True)
    print(result)


main()