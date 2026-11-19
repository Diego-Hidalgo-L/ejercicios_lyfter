from main import app
from flask import jsonify
from unittest.mock import MagicMock, patch
from datetime import date

def test_get_my_cart_with_existing_cart_and_owner_returns_200():
    # Arrange
    user_id = 1
    cart_id = 99
    mock_cart = {"id": cart_id, "user_id": user_id, "creation_date": str(date.today()), "cart_products": [], "status": "Active"}

    with(
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=None),
        patch("main.Cart.get_by_id_dict", return_value=mock_cart) as mock_get_cart,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}/carts/{cart_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json() == mock_cart
        mock_get_cart.assert_called_once_with(str(cart_id))
        mock_store_cache.assert_called_once()


def test_get_my_cart_with_inexistent_cart_returns_404():
    # Arrange
    user_id = 1
    cart_id = 99

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=None),
        patch("main.Cart.get_by_id_dict", return_value=None)
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}/carts/{cart_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 404
        assert response.get_json()["error_message"] == (f"Cart ID {cart_id} not found")


def test_get_my_cart_with_not_owner_returns_403():
    # Arrange
    user_id = 1
    cart_id = 99
    mock_cart = {"id": cart_id, "user_id": 2, "creation_date": str(date.today()), "cart_products": [], "status": "Active"}

    with(
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=None),
        patch("main.Cart.get_by_id_dict", return_value=mock_cart) as mock_get_cart,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}/carts/{cart_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 403
        assert response.get_json()["error_message"] == "Cannot access page"
        mock_get_cart.assert_called_once_with(str(cart_id))
        mock_store_cache.assert_not_called()


def test_get_my_cart_with_invalid_token_returns_401():
    # Arrange
    user_id = 1
    cart_id = 99

    client = app.test_client()

    with (
        patch("main.ioc.jwt_manager.decode", return_value=None),
        patch("main.Cart.get_by_id_dict") as mock_get_cart
    ):
        client = app.test_client()

    # Act
    response = client.get(
        f"/me/{user_id}/carts/{cart_id}",
        headers={"Authorization": "Bearer invalid_token"}
    )

    # Assert
    assert response.status_code == 401
    assert response.get_json()["error_message"] == "Error decoding token"
    mock_get_cart.assert_not_called()