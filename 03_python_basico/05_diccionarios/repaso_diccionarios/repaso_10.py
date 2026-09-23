
keys_to_remove = ["password", "token"]
user = {"username": "admin", "password": "1234"}
new_user_dict = {}

for key, value in user.items():
    if key not in keys_to_remove:
        new_user_dict[key] = value

print(new_user_dict)