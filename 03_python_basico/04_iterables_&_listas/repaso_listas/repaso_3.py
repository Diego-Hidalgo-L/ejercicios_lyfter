
my_list = [10, 20, 30, 40]

# last = my_list.pop(-1)
# my_list.insert(0, last)

rotated = [my_list[-1]] + my_list[:-1] # Mejor - no muta la lista original.

print(rotated)

