
product_price = int(input("Ingrese el precio del producto: "))

if product_price >= 100:
    discount = product_price * 0.10
else:
    discount = product_price * 0.02

final_price = product_price - discount

print("El precio final del producto es:", final_price)