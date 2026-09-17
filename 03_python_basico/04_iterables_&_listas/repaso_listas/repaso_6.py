
words = ["python", "code", "iterable", "loop", "dictionary"]

word_count = 0
target = 5

    # Opción 1: La MEJOR
word_count = sum(1 for word in words if len(word) > target)

    # Opción 2: La que pude haber pensado.
# for word in words:
#     if len(word) > target:
#         word_count += 1


    # Opción 3: La primera que pensé.
# for word in words:
#     letter_count = 0
#     for char in word:
#         letter_count += 1
#     if letter_count > target:
#         word_count += 1


print(f"Hay {word_count} palabras con más de {target} letras.")