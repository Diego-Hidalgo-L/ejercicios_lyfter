
def write_txt_file(path, text):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)


def read_txt_file(path):
    read_text = ""
    line_count = 0

    with open(path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            read_text += line
            line_count += 1

    split_text = read_text.split()

    return read_text, split_text, line_count


def count_chars_and_spaces(read_text):
    total_chars = len(read_text)
    no_spaces = 0

    for char in read_text:
        if char != " " or char != "\n":
            no_spaces += 1

    return total_chars, no_spaces


def find_longest_word_and_normalize_list(split_text):
    num_words = len(split_text)
    longest_word = None
    longest_count = 0
    longest_word_dict = {}
    normalized_list = []

    for word in split_text:
        normal_word = ""
        char_count = 0
        for char in word:
            if not char.isalpha():
                continue
            normal_word += char
            char_count += 1
        normalized_list.append(normal_word)

        if longest_word is None or char_count > longest_count:
            longest_word = normal_word
            longest_count = char_count
    
    longest_word_dict[longest_word] = longest_count

    return num_words, longest_word_dict, normalized_list


def find_most_common_word(normalized_list):
    word_dict = {}
    highest_word = None
    highest_num = 0
    highest_word_dict = {}
    
    for word in normalized_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    
    for word, num in word_dict.items():
        if highest_word is None or num > highest_num:
            highest_word = word
            highest_num = num
    
    highest_word_dict[highest_word] = highest_num

    return highest_word_dict


def convert_text_to_uppercase(read_text):
    return read_text.upper()


def write_report(path, report_text):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(report_text)


def main():
    text = """Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
before known,
Arouse! for you must justify me.

I myself but write one or two indicative words for the future,
I but advance a moment only to wheel and hurry back in the darkness.

I am a man who, sauntering along without fully stopping, turns a
casual look upon you and then averts his face,
Leaving it to you to prove and define it,
Expecting the main things from you."""

    write_txt_file('semana_18/ejercicios/file_handling/exercise_2/walt.txt', text)
    read_text, split_text, line_count = read_txt_file('semana_18/ejercicios/file_handling/exercise_2/walt.txt')
    total_chars, no_spaces = count_chars_and_spaces(read_text)
    num_words, longest_word_dict, normalized_list = find_longest_word_and_normalize_list(split_text)
    most_common_word_dict = find_most_common_word(normalized_list)
    upper_text = convert_text_to_uppercase(read_text)

    report_text = f"""Report:
\nTotal number of lines: {line_count}
Total number of words: {num_words}
Total number of characters (with spaces): {total_chars}
Total number of characters (NO spaces): {no_spaces}
Longest word: {list(longest_word_dict.keys())[0]} ({list(longest_word_dict.values())[0]})
The most common word: {list(most_common_word_dict.keys())[0]} ({list(most_common_word_dict.values())[0]})
\nUppercase text:
\n{upper_text}"""

    write_report('semana_18/ejercicios/file_handling/exercise_2/report.txt', report_text)


main()

