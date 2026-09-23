
def longest_word(my_list):
    longest_count = 0

    for word in my_list:
        count = 0
        for char in word:
            count += 1
        if count > longest_count:
            longest_count = count
            long_word = word
    return long_word


# print(longest_word(["short", "shore", "shot"]))

def longest_word_with_max_method(my_list):
    longest = max(my_list)
    print(longest)

# longest_word_with_max_method(["short", "shore", "shot"])


def longest_prefix(my_list):
    prefix = ''
    comp_word = my_list[-1]

    for index in range(len(comp_word)):
        current_char = comp_word[index]

        for word in my_list:
            if index >= len(word) or word[index] != current_char:
                return prefix
        
        prefix += current_char
    
    return prefix


print(longest_prefix(["short", "shore", "shot"]))
print(longest_prefix(["apple", "application", "appetizer"]))
print(longest_prefix(["", "b"]))
