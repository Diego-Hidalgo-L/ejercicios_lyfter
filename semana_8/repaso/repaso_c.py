
import csv

def write_products_csv(path, data, headers):
    with open(path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)


def main():
    products = [
    {"name": "TV", "price": 500},
    {"name": "Radio", "price": 80}
]
    write_products_csv('semana_8/repaso/products.csv', products, products[0].keys())


main()