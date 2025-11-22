def main():
	my_second_string = 'Hello'

	try:
		my_second_int = int(my_second_string)
		print(my_second_int + 2)
	except ValueError:
		print('Hubo un error al convertir este string a numero!')


if __name__ == '__main__':
	main()