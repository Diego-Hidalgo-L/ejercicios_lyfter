
# 

list_of_sales = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]

sale_data = ['date', 'customer_email', 'items']
item_data = ['name', 'upc', 'unit_price']

sales_per_upc_dict = {}

for sale_dict in list_of_sales:
    items_list = sale_dict.get('items')

    for item in items_list:
        upc = item.get('upc')
        unit_price = item.get('unit_price')
        
        if upc in sales_per_upc_dict: # Esto verifica si ya tengo un upc con el mismo valor en ese dict.
            sales_per_upc_dict[upc] += unit_price # Esto le suma el nuevo unit_price al valor que ya tenía.
        else:
            sales_per_upc_dict[upc] = unit_price # Esto NO es un append. Sobrescribe, no agrega. Por eso antes no me funcionaba.

print(sales_per_upc_dict)



