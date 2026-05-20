

def count_words(my_str):
    word_dict = {}
    word_list = my_str.lower().split()

    for w in word_list:
        # Mejora opcional:
        # word_dict[w] = word_dict.get(w, 0) + 1
        if w not in word_dict:
            word_dict[w] = 1
        else:
            word_dict[w] += 1
    
    return word_dict


def main():
    my_str = "Hola hola mundo cruel"
    word_dict = count_words(my_str)
    print(word_dict)


main()