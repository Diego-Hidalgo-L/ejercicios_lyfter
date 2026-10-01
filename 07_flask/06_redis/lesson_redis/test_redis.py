import redis

redis_client = redis.Redis(
    host="superclear-coppery-society-30341.db.redis.io",
    port=15592,
    password="9X5AZHxdmcIfMHOTV3m7J1ahmgtT8h3U"
)

try:
    connection_status = redis_client.ping()
    
    if connection_status:
        print("Connected to Redis!")
    else:
        print("The connection to Redis was unsuccessful!")

except redis.ConnectionError as ex:
    print("An error occurred while connecting to Redis: ", ex)


# Es útil y buena práctica utilizar estos métodos en funciones propias para atrapar errores y mantener el código lo más limpio posible, como se puede ver en la lección.
# Esas funciones las metemos en una clase y así hacemos el código más robusto, seguro y reutilizable.


# SET DATA:
# redis_client.set("first_key", "Este es mi primer valor por código guardado en Redis")
# redis_client.set("expiring_key", "Important value!", 10) # Ya no se utiliza .setex(), ahora solo se le pasa el parámetro de segundos de expiración al final.
# Si creamos varios keys con el mismo nombre, se van sobre escribiendo (solo queda el último que se escribió)


# CHECK DATA:
# redis_client.set("important_key", "This will live only 100 seconds", 100)
# exists_result = redis_client.exists("important_key") # Retorna 1 (True) o 0 (False)
# ttl_result = redis_client.ttl("important_key") # Retorna el ttl en segundos
# print("Exists:", exists_result)
# print("TTL:", ttl_result)


# GET DATA:
# value = redis_client.get("first_key")
# print(value.decode('utf-8')) # Se hace .decode('utf-8') porque en realidad no devuelve un string sino info en bytes. Esto lo decodifica en el tipo de encoding más popular que existe (utf-8).


# DELETE DATA:
# redis_client.delete("important_key") # Para eliminar un key
# redis_client.flushdb() # Para eliminar TODOS los keys de la base de datos del caché (RISKY!)
# Tendría que crearse el caché de nuevo desde 0 - puede llegar a ser muy pesado para el servidor.
# De todas formas, no deberíamos tener nada longevo en el caché.


# DELETE DATA con patrones: (No entiendo completamente cómo funcionan los datos paginados)
for key in redis_client.scan_iter(match="getUsers:*"): # Al parecer también funciona sin el key parameter 'match'
    print("Key to delete:", key.decode('utf-8'))
    redis_client.delete(key.decode('utf-8'))