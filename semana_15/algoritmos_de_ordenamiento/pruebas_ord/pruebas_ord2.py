

my_list = [19, 78, -3, 81, 34, 35, 67]

level = 0
for outer_index in range(len(my_list) - 1, - 1, -1):
    print(f"Level: {level}")
    for index in range(len(my_list) - 1, - 1 + level, -1):
        current_number = my_list[index]
        print(current_number)
    
    level += 1

# multiplier = 1

# while multiplier <= 5:
#     print(f"Multiplier: {multiplier}")
#     multiplier += 1