
purchases = [
    {"email": "a@gmail.com", "amount": 30},
    {"email": "b@gmail.com", "amount": 50},
    {"email": "a@gmail.com", "amount": 20},
]

new_purchases = {}

for purchase in purchases:
    email = purchase.get("email")
    amount = purchase.get("amount")

    new_purchases[email] = new_purchases.get(email, 0) + amount

    # if email not in new_purchases:
    #     new_purchases[email] = amount
    # else:
    #     new_purchases[email] += amount


print(new_purchases)