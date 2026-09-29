from flask import Flask, jsonify
from cache import CacheManager
from repositories import user_repository

app = Flask("users-service")

cache_manager = CacheManager(
    host="superclear-coppery-society-30341.db.redis.io",
    port=15592,
    password="9X5AZHxdmcIfMHOTV3m7J1ahmgtT8h3U"
)


def generate_cache_users_page_key(page):
    return f'getUsers-page{page}'


@app.route('/users/{page}/', methods=['GET'])
def get_users(page):
		page_key = generate_cache_users_page_key(page)
		if cache_manager.check_key(page_key):
			return cache_manager.get_data(page_key)
		else: # Si no existe en caché
			results = user_repository.get_all()
			# Toda la lógica para acceder a los datos en DB + cachear las páginas

@app.route('/update_user/{_id}', methods=['POST'])
def update_user(_id):
    # Toda la lógica para actualizar el usuario

		# Eliminación de las paginas cacheadas
    cache_manager.delete_data_with_pattern("getUsers-page")

    return jsonify({'status': 'user updated'})