from ioc_container import ioc

from flask import jsonify
import json


def check_if_cache(key):
    if ioc.cache_manager.check_key(key)[0]:
        cached_data = json.loads(ioc.cache_manager.get_data(key))
        return jsonify(cached_data), 200
    else:
        return None


def invalidate_cache(item, item_id=None, identifier=None): # Debería separar estas invalidaciones en 'single' y 'all'?
    if identifier is None:
        single_key = ioc.cache_manager.generate_key(item, item_id)
        all_key = ioc.cache_manager.generate_key(item, "all")
    else:
        single_key = ioc.cache_manager.generate_users_key(item, item_id, identifier)
        all_key = ioc.cache_manager.generate_users_key(item, "all", identifier)

    # CHECK AND INVALIDATE SINGLE ITEM CACHE:
    if item_id is not None and item_id != "all":
        single_check = ioc.cache_manager.check_key(single_key)

        if single_check[0]:
            delete_cache = ioc.cache_manager.delete_data(single_key)
            print("Single item cache invalidated successfully:", delete_cache)
        else:
            print("No single item cache to invalidate")

    # CHECK AND INVALIDATE 'ALL' CACHE:
    all_check = ioc.cache_manager.check_key(all_key)

    if all_check[0]:
        delete_cache = ioc.cache_manager.delete_data(all_key)
        print("'All' cache invalidated successfully:", delete_cache)
    else:
        print("No 'all' cache to invalidate")