
# Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.

first_list = ['Hay', 'en', 'que', 'iteración', 'índices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'útil']

combined_text = []

for index in range(0, len(first_list)):
    combined_text.append(first_list[index])
    combined_text.append(second_list[index])

print(combined_text)