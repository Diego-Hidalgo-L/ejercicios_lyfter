
def return_list_with_words_of_minimum_length(my_list):
    new_list = []
    min_len = int(input("Enter the minimum amount of characters you want the words to be: "))

    for word in my_list:
        if len(word) >= min_len:
            new_list.append(word)
    
    return new_list


def main():
    my_list = ["cielo", "sol", "maravilloso", "día"]
    new_list = return_list_with_words_of_minimum_length(my_list)
    print(new_list)