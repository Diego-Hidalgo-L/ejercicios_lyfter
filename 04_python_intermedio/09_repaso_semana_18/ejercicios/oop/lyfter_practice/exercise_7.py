
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def get_value(self):
        return self.price * self.quantity 


class Inventory:
    def __init__(self):
        self.products_list = []
    
    def add_product(self, product):
        self.products_list.append(product)

    def show_all_products(self):
        for product in self.products_list:
            print(f"Product: {product.name}")
            print(f"Price: {product.price}")
            print(f"Quantity: {product.quantity}")
            print()

    def calculate_total_value(self):
        total_value = 0

        for product in self.products_list:
            total_value += product.get_value()
        
        return total_value


product1 = Product("Mouse", 5000, 3)
product2 = Product("Teclado", 8000, 2)

my_inventory = Inventory()

def main():
    my_inventory.add_product(product1)
    my_inventory.add_product(product2)

    my_inventory.show_all_products()
    total_value = my_inventory.calculate_total_value()
    print(f"Total value: {total_value}")

main()