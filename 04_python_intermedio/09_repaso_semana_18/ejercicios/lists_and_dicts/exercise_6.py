

def calculate_revenue_by_upc(sales):
    data = {}

    for sale in sales:
        for item in sale.get('items'):
            upc = item.get('upc')
            unit_price = item.get('unit_price')

            if upc in data:
                data[upc] += unit_price
            else:
                data[upc] = unit_price
    
    return data


def calculate_highest_upc(data):
    highest_upc = None
    highest_revenue = None

    for upc, revenue in data.items():
        if highest_revenue is None or revenue > highest_revenue:
            highest_upc = upc
            highest_revenue = revenue
    
    return highest_upc, highest_revenue


def print_messages(data, highest_upc, highest_revenue):
    for upc, revenue in data.items():
        print(f"{upc}: ${revenue:.2f}")
    
    print(f"The UPC with the highest total revenue was: {highest_upc} (${highest_revenue:.2f})")


def main():
    sales = [

    {'date':'2024-01-01','email':'a@x.com','items':[
        {'name':'Lamp','upc':'ITEM-1','unit_price':30.00},

        {'name':'Fan','upc':'ITEM-2','unit_price':45.50},

    ]},

    {'date':'2024-01-02','email':'b@x.com','items':[
        {'name':'Lamp','upc':'ITEM-1','unit_price':30.00},

        {'name':'Mat','upc':'ITEM-3','unit_price':12.00},

    ]},

    {'date':'2024-01-02','email':'c@x.com','items':[
        {'name':'Fan','upc':'ITEM-2','unit_price':45.50},

        {'name':'Fan','upc':'ITEM-2','unit_price':45.50},

    ]},

    ]

    data = calculate_revenue_by_upc(sales)
    highest_upc, highest_revenue = calculate_highest_upc(data)
    print_messages(data, highest_upc, highest_revenue)


main()