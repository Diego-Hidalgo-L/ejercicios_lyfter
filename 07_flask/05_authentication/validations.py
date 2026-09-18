from ioc_container import ioc
from flask import jsonify

# Podría convertir este role validation en una función, un método o un decorator. Cuál sería mejor?
    # No lo hice decorator, porque los decorators reciben los mismos parámetros de la función que están decorando.
    # Este validation solo recibe un token que se obtiene desde ADENTRO de la función, no como parámetro de esa función.

def validate_if_admin(token):
    if token is None:
        return jsonify(error_message="Invalid token"), 422       # 422 o 400?

    test_token = token.replace("Bearer ","")
    decoded = ioc.jwt_manager.decode(test_token)

    if decoded is None:
        return jsonify(error_message="Error decoding token"), 500

    user_id = decoded['id']
    user = ioc.users_repo.get_user_by_id(user_id)

    if user is None:
        return jsonify(error_message="User not found"), 404

    user_role = user[3]

    if user_role != "Administrator":
        return jsonify(error_message="Cannot access page"), 401

    return True


def validate_if_same_user_or_admin(token, identifier):
    if token is None:
        return False, (jsonify(error_message="Invalid token"), 422 )     # 422 o 400?

    user_id = ioc.users_repo.get_user_by_id(identifier)[0]

    if user_id is None:
        return False, (jsonify(error_message=f"User ID {identifier} not found"), 404)

    test_token = token.replace("Bearer ", "")
    decoded_user_id = ioc.jwt_manager.decode(test_token)['id']
    decoded_user_role = ioc.users_repo.get_user_by_id(decoded_user_id)[3]

    if user_id != decoded_user_id and decoded_user_role != "Administrator":
        return False, (jsonify(error_message="Cannot access page"), 401)

    return True, user_id