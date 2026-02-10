
products = [
    {"name": "TV", "category": "Electrónica", "price": 500},
    {"name": "Radio", "category": "Electrónica", "price": 80},
    {"name": "Sofá", "category": "Muebles", "price": 700},
]

result = {}

for product in products:
    category = product.get("category")
    price = product.get("price")

    if result.get(category) is None:
        result[category] = 0

    if price > result[category]:
        result[category] = price


print(result)