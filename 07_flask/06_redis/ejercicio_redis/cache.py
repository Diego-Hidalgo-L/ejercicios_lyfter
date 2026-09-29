import redis
import json


class CacheManager:
    def __init__(self, host, port, password, *args, **kwargs):
        self.redis_client = redis.Redis(
            host=host,
            port=port,
            password=password,
            *args,
            **kwargs,
        )
        connection_status = self.redis_client.ping()
        if connection_status:
            print("Connection created successfully")


# ------------------- start PRODUCTS: -------------------
    def generate_product_key(self, identifier):
        return f"product:{identifier}"

    def store_product_data(self, key, product_id, name, price, entry_date, stock, time_to_live=None):
        try:
            data = {
                    "product_id": product_id,
                    "name": name,
                    "price": price,
                    "entry_date": str(entry_date),
                    "stock": stock
                }

            if time_to_live is None:
                self.redis_client.set(key, json.dumps(data))

            else:
                self.redis_client.set(key, json.dumps(data), time_to_live)

            print("Data cached successfully")

        except redis.RedisError as error:
            print(f"An error occurred while storing data in Redis: {error}")

# ------------------- end PRODUCTS: -------------------

    def store_data(self, key, value, time_to_live=None):
        try:
            if time_to_live is None:
                self.redis_client.set(key, value)
            else:
                self.redis_client.set(key, value, time_to_live)

        except redis.RedisError as error:
            print(f"An error occurred while storing data in Redis: {error}")

    def check_key(self, key):
        try:
            key_exists = self.redis_client.exists(key)

            if key_exists:
                ttl = self.redis_client.ttl(key)
                return True, ttl
            else:
                return False, None
            
        except redis.RedisError as error:
            print(f"An error occurred while checking a key in Redis: {error}")
            return False, None

    def get_data(self, key):
        try:
            output = self.redis_client.get(key)
            if output is not None:
                result = output.decode("utf-8")
                return result
            else:
                return None
            
        except redis.RedisError as error:
            print(f"An error occurred while retrieving data from Redis: {error}")

    def delete_data(self, key):
        try:
            output = self.redis_client.delete(key)
            return output == 1

        except redis.RedisError as error:
            print(f"An error occurred while deleting data from Redis: {error}")
            return False

    def delete_data_with_pattern(self, pattern):
        try:
            # Iterar sobre las claves que coinciden con el patrón
            for key in self.redis_client.scan_iter(match=pattern):
                self.delete_data(key)

        except redis.RedisError as error:
            print(f"An error occurred while deleting data from Redis: {error}")