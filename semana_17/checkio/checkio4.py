
def reverse_digits(num):
    num = str(num)
    new_num = ''

    for index in range(len(num) - 1, - 1, - 1):
        digit = num[index]
        new_num += str(digit)
    
    return new_num

reverse_digits(1234)

