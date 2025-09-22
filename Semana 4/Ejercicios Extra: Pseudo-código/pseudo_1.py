# Cree un pseudocódigo que le pida un precio de producto al usuario.
# Calcule su descuento y muestre el precio final tomando en cuenta que:
    # Si el precio es menor a 100, el descuento es del 2%.
    # Si el precio es mayor o igual a 100, el descuento es del 10%.


product_price = float(input("Please enter the product's price: "))

if (product_price >= 100):
    discount = product_price * 0.10
else:
    discount = product_price * 0.02

final_price = product_price - discount

print (f"The product's final price is: {final_price}")