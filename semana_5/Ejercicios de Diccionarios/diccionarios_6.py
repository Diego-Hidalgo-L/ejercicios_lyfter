
# Dada una lista de productos vendidos, donde cada uno tiene categoría y precio.
# Cree un diccionario que acumule el total por categoría.

products_dict = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

dict_by_category = {}

for product in products_dict:
    category = product.get("category")
    # name = product.get("name") # No hago nada con el "name"
    price = product.get("price")

    if category in dict_by_category:
        dict_by_category[category] += price
    else:
        dict_by_category[category] = price

print(dict_by_category)


