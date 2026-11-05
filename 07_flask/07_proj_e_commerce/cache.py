import redis
import random


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

    def generate_key(self, item, item_id):
        return f"{item}:{item_id}"

    def generate_users_key(self, identifier, item, item_id=None):
        if item_id is None:
            return f"users:{identifier}:{item}:all"
        else:
            return f"users:{identifier}:{item}:{item_id}"

    def store_data(self, key, data, ttl=None, jitter=30):
        try:
            if ttl is not None:
                final_ttl = ttl + random.randint(0, jitter)
            else:
                final_ttl = None

            self.redis_client.set(key, data, final_ttl)
            print("Data cached successfully")
            print(f"TTL: {final_ttl}")

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

    def expire(self, key, exp):
        try:
            self.redis_client.expire(key, exp)

        except redis.RedisError as error:
            print(f"An error occurred while setting new expiry time: {error}")