from ioc_container import ioc
from flask import Response, jsonify

# Podría convertir este role validation en una función, un método o un decorator. Cuál sería mejor?
    # No lo hice decorator, porque los decorators reciben los mismos parámetros de la función que están decorando.
    # Este validation solo recibe un token que se obtiene desde ADENTRO de la función, no como parámetro de esa función.

def validate_if_admin(token):
    if token is None:
        return jsonify(error_message="Invalid token"), 401

    test_token = token.replace("Bearer ","")
    decoded = ioc.jwt_manager.decode(test_token)

    if decoded is None:
        return jsonify(error_message="Error decoding token"), 401

    user_id = decoded['id']
    user = ioc.users_repo.get_user_by_id(user_id)

    if user is None:
        return jsonify(error_message="User not found"), 404

    user_role = user[3]

    if user_role != "Administrator":
        return jsonify(error_message="Cannot access page"), 403

    return True


def validate_if_same_user_or_admin(token, identifier):
    if token is None:
        return False, (jsonify(error_message="Invalid token"), 401)

    user = ioc.users_repo.get_user_by_id(identifier)

    if user is None:
        return False, (jsonify(error_message=f"User ID {identifier} not found"), 404)

    user_id = user[0]
    test_token = token.replace("Bearer ", "")
    decoded = ioc.jwt_manager.decode(test_token)

    if decoded is None:
        return False, (jsonify(error_message="Error decoding token"), 401)

    decoded_user_id = decoded['id']
    decoded_user_role = user[3]

    if user_id != decoded_user_id and decoded_user_role != "Administrator":
        return False, (jsonify(error_message="Cannot access page"), 403)

    return True, user_id