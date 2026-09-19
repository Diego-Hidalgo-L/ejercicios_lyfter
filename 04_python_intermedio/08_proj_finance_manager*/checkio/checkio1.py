
def translation(text):
    letters = "aeiouy"
    new = ''
    index = 0
    while index < len(text):
        if text[index] == ' ':
            new += text[index]
        elif text[index] not in letters and text[index + 1] in letters:
            new += text[index]
            index += 1
        elif text[index] in letters:
            if text[index:index + 3] == text[index] * 3:
                new += text[index]
                index += 2
        index += 1
    return new

print(translation("hoooowe yyyooouuu duoooiiine"))