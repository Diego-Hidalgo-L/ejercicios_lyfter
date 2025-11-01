
max_pass = 20
total_pass = 0
changer = 0

while changer == 0:
    current_pass = int(input("How many passengers want to get on the bus? "))

    total_pass += current_pass

    if total_pass <= max_pass:
        print(f"Passengers loaded. Amount of passengers: {total_pass}")
    else:
        print(f"Amount of passengers: {total_pass}. No more passengers allowed.")
        break

    changer = int(input("Type '0' if you wish to continue and '1' if you wish to stop: "))