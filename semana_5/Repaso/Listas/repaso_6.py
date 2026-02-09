
words = ["python", "code", "iterable", "loop", "dictionary"]

word_count = 0
target = 5

for word in words:
    letter_count = 0
    for char in word:
        letter_count += 1
    if letter_count > target:
        word_count += 1


print(f"Hay {word_count} palabras con más de {target} letras.")