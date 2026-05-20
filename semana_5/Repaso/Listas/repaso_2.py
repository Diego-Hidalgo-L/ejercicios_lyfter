
text = "Iterables"
new_text = ""

for i in range(len(text) -1, -1, -1):
    new_text += text[i]


print(new_text)