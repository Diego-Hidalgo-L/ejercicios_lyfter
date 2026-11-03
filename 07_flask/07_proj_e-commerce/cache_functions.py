from flask import jsonify
import json
from ioc_container import ioc


def check_if_cache(item, identifier):
    key = ioc.cache_manager.generate_key(item, identifier) # Debería generar este key afuera de la función? Demasiadas acciones dentro de una misma función?
    
    if ioc.cache_manager.check_key(key)[0]:
        cached_data = json.loads(ioc.cache_manager.get_data(key))
        
        return jsonify(cached_data), 200
    
    return None, key


def invalidate_cache(item, identifier):
    # CHECK AND INVALIDATE SINGLE ITEM CACHE:
    single_key = ioc.cache_manager.generate_key(item, identifier)
    single_check = ioc.cache_manager.check_key(single_key)

    if single_check[0]:
        delete_cache = ioc.cache_manager.delete_data(single_key)
        print("Single product cache invalidated successfully:", delete_cache)
    else:
        print("No single cache to invalidate")

    # CHECK AND INVALIDATE 'ALL' CACHE:
    all_key = ioc.cache_manager.generate_key(item, "all")
    all_check = ioc.cache_manager.check_key(all_key)

    if all_check[0]:
        delete_cache = ioc.cache_manager.delete_data(all_key)
        print("'All' Cache invalidated successfully:", delete_cache)
    else:
        print("No 'all' cache to invalidate")