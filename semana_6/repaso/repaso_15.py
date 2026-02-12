
def check_if_palindrome(my_str):
    str_list = my_str.lower().split()
    uni_str = "".join(str_list)

    return uni_str == uni_str[::-1]


def main():
    my_str = "Anita lava la tina"
    second_str = "Hola mundo cruel"
    if_palindrome = check_if_palindrome(second_str)
    print("¿El string es un palíndromo?",if_palindrome)

main()