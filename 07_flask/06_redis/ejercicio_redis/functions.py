import random
from ioc_container import ioc

# data = {'id': 12}
# access_token = ioc.jwt_manager.encode(data, "access")
# decoded_access = ioc.jwt_manager.decode(access_token)
# print({"access_token":access_token, "decoded":{decoded_access['id'], decoded_access['token_type']}})

# print("\n")

# refresh_token = ioc.jwt_manager.encode(data, "refresh")
# decoded_refresh = ioc.jwt_manager.decode(refresh_token)
# print({"access_token":refresh_token, "decoded":{decoded_refresh['id'], decoded_refresh['token_type']}})


def generate_fake_ip():
    numbers = []

    for _ in range(4):
        number = random.randint(0, 255)
        numbers.append(str(number))

    fake_ip = ".".join(numbers)
    return fake_ip