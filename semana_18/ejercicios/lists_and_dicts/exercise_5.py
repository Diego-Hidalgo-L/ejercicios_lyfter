
# Part A:
def calculate_average(my_list):
    total_sum = 0
    for n in my_list:
        total_sum += n

    return round(total_sum / len(my_list), 2)


def create_above_average_list(my_list, avg):
    above_avg_list = []
    for n in my_list:
        if n > avg:
            above_avg_list.append(n)
    
    return above_avg_list


# Part B:
def input_words(WORD_TARGET):
    while True:
        words_str = input("Please enter 6 words separated by spaces: ")
        words_list = words_str.split()

        if len(words_list) == WORD_TARGET:
            break

        print("Please enter exactly 6 words.")
    
    return words_str, words_list


def filter_list(CHAR_TARGET, words_list):
    filtered_list = []

    for word in words_list:
        if len(word) > CHAR_TARGET:
            filtered_list.append(word)

    return filtered_list


def bubble_sort(filtered_list):
    for outer_index in range(0, len(filtered_list) - 1):
        has_made_changes = False

        for index in range(0, len(filtered_list) - 1 - outer_index):
            current_element = filtered_list[index]
            next_element = filtered_list[index + 1]

            if current_element > next_element:
                filtered_list[index] = next_element
                filtered_list[index + 1] = current_element
                has_made_changes = True
        
        if not has_made_changes:
            break


# Execution:
def execute_a():
    my_list = [10, 20, 30, 40, 50, 15, 25]

    avg = calculate_average(my_list)
    above_avg_list = create_above_average_list(my_list, avg)

    print(f"Average: {avg}")
    print(f"Above average: {above_avg_list}")


def execute_b():
    # split_list = ['cat', 'elephant', 'sun', 'programming', 'loop', 'sky']
    WORD_TARGET = 6
    CHAR_TARGET = 4

    words_str, words_list = input_words(WORD_TARGET)
    filtered_list = filter_list(CHAR_TARGET, words_list)

    print(f"Input: {words_str}")
    print(f"Filtered (>4 chars): {filtered_list}")
    
    bubble_sort(filtered_list)
    print(f"Sorted: {filtered_list}")


def main():
    execute_a()
    execute_b()


main()