from main import app
from db import User

from flask import jsonify
from unittest.mock import patch
from argon2.exceptions import VerifyMismatchError


# ------------------- POST TESTS start -------------------

def test_register_with_valid_credentials_returns_201():
    # Arrange
    request_json = {"username": "user_123", "password": "123", "email": "user_123@gmail.com", "full_name": "User 123"}
    mock_user = User(id=1, username="user_123", password="123", email="user_123@gmail.com", full_name="User 123", role="User")

    with (
        patch("main.User.add", return_value=mock_user) as mock_add_user,
        patch("main.ioc.jwt_manager.encode", side_effect=["fake_access_token", "fake_refresh_token"]) as mock_encode,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.post(
            "/register",
            json=request_json
        )

        # Assert
        assert response.status_code == 201
        assert response.get_json() == {"access_token": "fake_access_token", "refresh_token": "fake_refresh_token"}
        mock_add_user.assert_called_once()
        assert mock_encode.call_count == 2
        mock_invalidate_cache.assert_called_once_with("users", "all")


def test_register_with_incomplete_credentials_returns_400():
    # Arrange
    password = None
    request_json = {"username": "default_user", "password": password, "email": "user_123@gmail.com", "full_name": "User 123"}

    with (
        patch("main.User.add") as mock_add_user,
        patch("main.ioc.jwt_manager.encode") as mock_encode,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.post(
            "/register",
            json=request_json
        )

        # Assert
        assert response.status_code == 400
        assert response.get_json()["error_message"] == "Invalid credentials"
        mock_add_user.assert_not_called()
        mock_encode.assert_not_called()
        mock_invalidate_cache.assert_not_called()


def test_login_with_successful_login_returns_200():
    # Arrange
    username = "user_123"
    request_json = {"username": username, "password": "fake_hashed_password"}
    mock_user = User(id=1, username=username, password="fake_hashed_password", email="user_123@gmail.com", full_name="User 123", role="User")

    with (
        patch("main.User.get_by_username", return_value=mock_user) as mock_get_user,
        patch("main.ioc.ph") as mock_password_hasher,
        patch("main.ioc.jwt_manager.encode", side_effect=["fake_access_token", "fake_refresh_token"]) as mock_encode
    ):
        client = app.test_client()

        # Act
        response = client.post(
            "/login",
            json=request_json
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json() == {"access_token": "fake_access_token", "refresh_token": "fake_refresh_token"}
        mock_get_user.assert_called_once_with(username)
        mock_password_hasher.verify.assert_called_once_with(mock_user.password, request_json['password'])
        assert mock_encode.call_count == 2


def test_login_with_inexistent_user_returns_404():
    # Arrange
    username = "user_123"
    request_json = {"username": username, "password": "incorrect_password"}

    with (
        patch("main.User.get_by_username", return_value=None) as mock_get_user,
        patch("main.ioc.ph") as mock_password_hasher,
        patch("main.ioc.jwt_manager.encode") as mock_encode
    ):
        client = app.test_client()

        # Act
        response = client.post(
            "/login",
            json=request_json
        )

        # Assert
        assert response.status_code == 404
        assert response.get_json()["error_message"] == "User not found"
        mock_get_user.assert_called_once_with(username)
        mock_password_hasher.verify.assert_not_called()
        mock_encode.assert_not_called()


def test_login_with_incorrect_password_returns_400():
    # Arrange
    username = "user_123"
    request_json = {"username": username, "password": "incorrect_password"}
    mock_user = User(id=1, username=username, password="fake_hashed_password", email="user_123@gmail.com", full_name="User 123", role="User")

    with (
        patch("main.User.get_by_username", return_value=mock_user) as mock_get_user,
        patch("main.ioc.ph") as mock_password_hasher,
        patch("main.ioc.jwt_manager.encode") as mock_encode
    ):
        mock_password_hasher.verify.side_effect = VerifyMismatchError
        
        client = app.test_client()

        # Act
        response = client.post(
            "/login",
            json=request_json
        )

        # Assert
        assert response.status_code == 400
        assert response.get_json()["error_message"] == "Invalid credentials"
        mock_get_user.assert_called_once_with(username)
        mock_password_hasher.verify.assert_called_once_with(mock_user.password, request_json['password'])
        mock_encode.assert_not_called()


def test_refresh_token_with_valid_token_returns_200():
    # Arrange
    token = "Bearer fake_token"
    user_id = 1
    decoded = {"id": user_id, "token_type": "refresh"}

    with (
        patch("main.ioc.jwt_manager.decode", return_value=decoded) as mock_decode,
        patch("main.ioc.jwt_manager.encode", return_value="fake_access_token") as mock_encode
    ):
        client = app.test_client()

        # Act
        response = client.post(
            "/refresh-token",
            headers={"Authorization": token}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json() == {"access_token": "fake_access_token"}
        mock_decode.assert_called_once_with(token)
        mock_encode.assert_called_once_with(user_id, "access")


def test_refresh_token_with_no_token_returns_401():
    # Arrange
    with (
        patch("main.ioc.jwt_manager.decode") as mock_decode,
        patch("main.ioc.jwt_manager.encode") as mock_encode
    ):
        client = app.test_client()

        # Act
        response = client.post("/refresh-token")

        # Assert
        assert response.status_code == 401
        assert response.get_json()["error_message"] == "Invalid token"
        mock_decode.assert_not_called()
        mock_encode.assert_not_called()


def test_refresh_token_with_error_decoding_refresh_token_returns_401():
    # Arrange
    token = "Bearer fake_token"

    with (
        patch("main.ioc.jwt_manager.decode", return_value=None) as mock_decode,
        patch("main.ioc.jwt_manager.encode", return_value="fake_access_token") as mock_encode
    ):
        client = app.test_client()

        # Act
        response = client.post(
            "/refresh-token",
            headers={"Authorization": token}
        )

        # Assert
        assert response.status_code == 401
        assert response.get_json()["error_message"] == "Error decoding token"
        mock_decode.assert_called_once_with(token)
        mock_encode.assert_not_called()


def test_refresh_token_with_invalid_token_type_returns_400():
    # Arrange
    token = "Bearer fake_token"
    user_id = 1
    decoded = {"id": user_id, "token_type": "access"}

    with (
        patch("main.ioc.jwt_manager.decode", return_value=decoded) as mock_decode,
        patch("main.ioc.jwt_manager.encode") as mock_encode
    ):
        client = app.test_client()

        # Act
        response = client.post(
            "/refresh-token",
            headers={"Authorization": token}
        )

        # Assert
        assert response.status_code == 400
        assert response.get_json()["error_message"] == "Invalid token type"
        mock_decode.assert_called_once_with(token)
        mock_encode.assert_not_called()


def test_refresh_token_with_error_encoding_access_token_returns_401():
    # Arrange
    token = "Bearer fake_token"
    user_id = 1
    decoded = {"id": user_id, "token_type": "refresh"}

    with (
        patch("main.ioc.jwt_manager.decode", return_value=decoded) as mock_decode,
        patch("main.ioc.jwt_manager.encode", return_value=None) as mock_encode
    ):
        client = app.test_client()

        # Act
        response = client.post(
            "/refresh-token",
            headers={"Authorization": token}
        )

        # Assert
        assert response.status_code == 500
        assert response.get_json()["error_message"] == "Error encoding access token"
        mock_decode.assert_called_once_with(token)
        mock_encode.assert_called_once_with(user_id, "access")

# ------------------- POST TESTS end -------------------


# ------------------- GET TESTS start -------------------

def test_get_all_users_successfully_returns_200():
    # Arrange
    mock_user = {"id": 1, "username": "user_123", "password": "fake_hashed_password", "email": "user_123@gmail.com", "full_name": "User 123", "role": "User"}
    mock_users = [mock_user]

    with (
        patch("main.validate_admin", return_value=True),
        patch("main.check_if_cache", return_value=None),
        patch("main.User.get_all", return_value=mock_users) as mock_get_users,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            "/users",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json() == mock_users
        mock_get_users.assert_called_once
        mock_store_cache.assert_called_once()


def test_get_all_users_with_unauthorized_user_returns_403():
    # Arrange
    with (
        app.app_context(),
        patch("main.validate_admin") as mock_validate_admin,
        patch("main.User.get_all") as mock_get_users,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        mock_validate_admin.return_value = (jsonify(error_message="Cannot access page"), 403)
        
        client = app.test_client()

        # Act
        response = client.get(
            "/users",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 403
        assert response.get_json()["error_message"] == "Cannot access page"
        mock_get_users.assert_not_called()
        mock_store_cache.assert_not_called()


def test_me_with_own_profile_returns_200():
    # Arrange
    user_id = 1
    mock_user = User(id=user_id, username="user_123", password="fake_hashed_password", email="user_123@gmail.com", full_name="User 123", role="User")
    mock_user_dict = {"id": user_id, "username": "user_123", "password": "fake_hashed_password", "email": "user_123@gmail.com", "full_name": "User 123", "role": "User"}

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=None),
        patch("main.User.get_by_id", return_value=mock_user) as mock_get_user,
        patch("main.User.format_dict", return_value=mock_user_dict) as mock_get_user_dict,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json() == mock_user_dict
        mock_get_user.assert_called_once_with(user_id)
        mock_get_user_dict.assert_called_once()
        mock_store_cache.assert_called_once()


def test_me_with_unauthorized_user_returns_403():
    # Arrange
    user_id = 1

    with (
        app.app_context(),
        patch("main.validate_owner") as mock_validate_owner,
        patch("main.User.get_by_id") as mock_get_user,
        patch("main.User.format_dict") as mock_get_user_dict,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        mock_validate_owner.return_value = (jsonify(error_message="Cannot access page"), 403)
        
        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 403
        assert response.get_json()["error_message"] == "Cannot access page"
        mock_get_user.assert_not_called()
        mock_get_user_dict.assert_not_called()
        mock_store_cache.assert_not_called()

# ------------------- GET TESTS end -------------------


# ------------------- PATCH TESTS start -------------------

def test_update_user_successfully_returns_200():
    # Arrange
    user_id = "1"
    mock_user = User(id=user_id, username="user_123", password="fake_hashed_password", email="user_123@gmail.com", full_name="User 123", role="User")

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.User.get_by_id", return_value=mock_user) as mock_get_user,
        patch("main.User.update", return_value=True) as mock_update_user,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.patch(
            f"/users/{user_id}",
            headers={"Authorization": "Bearer fake_token"},
            json={"username": "user_456"}
        )

        # Arrange
        assert response.status_code == 200
        assert response.get_json()["message"] == f"User ID {user_id} updated successfully"
        mock_get_user.assert_called_once_with(user_id)
        mock_update_user.assert_called_once_with(username="user_456", password=None)
        mock_invalidate_cache.call_count == 2


def test_update_user_with_inexistent_user_returns_404():
    # Arrange
    user_id = "1"

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.User.get_by_id", return_value=None) as mock_get_user,
        patch("main.User.update", return_value=True) as mock_update_user,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.patch(
            f"/users/{user_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Arrange
        assert response.status_code == 404
        assert response.get_json()["error_message"] == f"User ID {user_id} not found"
        mock_get_user.assert_called_once_with(user_id)
        mock_update_user.assert_not_called()
        mock_invalidate_cache.assert_not_called()


def test_update_user_with_not_profile_owner_returns_403():
    # Arrange
    user_id = "1"

    with (
        app.app_context(),
        patch("main.validate_owner") as mock_validate_owner,
        patch("main.User.get_by_id") as mock_get_user,
        patch("main.User.update") as mock_update_user,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        mock_validate_owner.return_value = (jsonify(error_message="Cannot access page"), 403)

        client = app.test_client()

        # Act
        response = client.patch(
            f"/users/{user_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 403
        assert response.get_json()["error_message"] == "Cannot access page"
        mock_get_user.assert_not_called()
        mock_update_user.assert_not_called()
        mock_invalidate_cache.assert_not_called()

# ------------------- PATCH TESTS end -------------------


# ------------------- DELETE TESTS start -------------------

def test_delete_user_successfully_returns_200():
    # Arrange
    user_id = "1"
    mock_user = User(id=user_id, username="user_123", password="fake_hashed_password", email="user_123@gmail.com", full_name="User 123", role="User")

    with (
        patch("main.validate_owner_or_admin", return_value=(True, {"id": user_id})),
        patch("main.User.get_by_id", return_value=mock_user) as mock_get_user,
        patch("main.User.delete", return_value=True) as mock_delete_user,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.delete(
            f"/users/{user_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json()["message"] == f"User ID {user_id} deleted successfully"
        mock_get_user.assert_called_once_with(user_id)
        mock_delete_user.assert_called_once()
        mock_invalidate_cache.call_count == 2


def test_delete_user_with_with_inexistent_user_returns_404():
    # Arrange
    user_id = "1"

    with (
        patch("main.validate_owner_or_admin", return_value=(True, {"id": user_id})),
        patch("main.User.get_by_id", return_value=None) as mock_get_user,
        patch("main.User.delete", return_value=True) as mock_delete_user,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.delete(
            f"/users/{user_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Arrange
        assert response.status_code == 404
        assert response.get_json()["error_message"] == f"User ID {user_id} not found"
        mock_get_user.assert_called_once_with(user_id)
        mock_delete_user.assert_not_called()
        mock_invalidate_cache.assert_not_called()


def test_delete_user_with_not_profile_owner_returns_403():
    # Arrange
    user_id = "1"

    with (
        app.app_context(),
        patch("main.validate_owner_or_admin") as mock_validate_owner_or_admin,
        patch("main.User.get_by_id") as mock_get_user,
        patch("main.User.delete") as mock_delete_user,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        mock_validate_owner_or_admin.return_value = (jsonify(error_message="Cannot access page"), 403)

        client = app.test_client()

        # Act
        response = client.delete(
            f"/users/{user_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 403
        assert response.get_json()["error_message"] == "Cannot access page"
        mock_get_user.assert_not_called()
        mock_delete_user.assert_not_called()
        mock_invalidate_cache.assert_not_called()

# ------------------- DELETE TESTS end -------------------