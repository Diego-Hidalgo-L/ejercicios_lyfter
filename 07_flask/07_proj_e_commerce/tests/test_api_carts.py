from main import app
from db import Cart

from flask import jsonify
from unittest.mock import patch
from datetime import date


# ------------------- POST TESTS start -------------------

def test_add_active_cart_without_existing_cart_returns_200():
    # Arrange
    user_id = 1

    mock_cart_products = [{"product_id": 3, "quantity": 1, "total_price": 15}]
    mock_cart = Cart(id=99, user_id=user_id, creation_date=str(date.today()), status="Active")

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.Cart.get_or_create_active_cart", return_value=mock_cart) as mock_get_cart,
        patch("main.CartProduct.get_by_cart_id", return_value=mock_cart_products) as mock_get_cart_products,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.post(
            f"/me/{user_id}/carts",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json() == {"id": 99, "user_id": user_id, "creation_date": str(date.today()), "cart_products": mock_cart_products, "status": "Active"}
        mock_get_cart.assert_called_once_with(user_id)
        mock_get_cart_products.assert_called_once_with(99)
        mock_invalidate_cache.assert_called_once_with("carts", identifier=str(user_id))


def test_add_active_cart_with_error_creating_cart_raises_exception_and_returns_500():
    # Arrange
    user_id = 1

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.Cart.get_or_create_active_cart", return_value=False) as mock_get_cart,
        patch("main.CartProduct.get_by_cart_id") as mock_get_cart_products,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.post(
            f"/me/{user_id}/carts",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 500
        assert response.get_json()["error_message"] == "Error adding cart: Error creating active cart"
        mock_get_cart.assert_called_once_with(user_id)
        mock_get_cart_products.assert_not_called()
        mock_invalidate_cache.assert_not_called()

# ------------------- POST TESTS end -------------------


# ------------------- GET TESTS start -------------------

def test_get_all_my_carts_for_user_with_carts_returns_200():
    # Arrange
    user_id = 1

    mock_cart_1 = {"id": 99, "user_id": user_id, "creation_date": str(date.today()), "cart_products": [], "status": "Active"}
    mock_cart_2 = {"id": 98, "user_id": user_id, "creation_date": "2026-11-18", "cart_products": [], "status": "Abandoned"}
    mock_carts = [mock_cart_1, mock_cart_2]

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=None),
        patch("main.Cart.get_all_by_user_id", return_value=mock_carts) as mock_get_carts,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}/carts",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json() == mock_carts
        mock_get_carts.assert_called_once()
        mock_store_cache.assert_called_once()


def test_get_all_my_carts_for_user_with_no_carts_returns_404():
    # Arrange
    user_id = 1

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=None),
        patch("main.Cart.get_all_by_user_id", return_value=None) as mock_get_carts,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}/carts",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 404
        assert response.get_json()["error_message"] == "No carts found"
        mock_get_carts.assert_called_once()
        mock_store_cache.assert_not_called()


def test_get_all_my_carts_from_cache_returns_200():
    # Arrange
    user_id = 1

    mock_cart_1 = {"id": 99, "user_id": user_id, "creation_date": str(date.today()), "cart_products": [], "status": "Active"}
    mock_cart_2 = {"id": 98, "user_id": user_id, "creation_date": "2026-11-18", "cart_products": [], "status": "Abandoned"}
    mock_carts_cache = [mock_cart_1, mock_cart_2]

    with (
        app.app_context(),
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=jsonify(mock_carts_cache)),
        patch("main.Cart.get_all_by_user_id") as mock_get_carts,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}/carts",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json() == mock_carts_cache
        mock_get_carts.assert_not_called()
        mock_store_cache.assert_not_called()


def test_get_my_cart_with_existing_cart_and_owner_returns_200():
    # Arrange
    user_id = 1
    cart_id = 99
    mock_cart = {"id": cart_id, "user_id": user_id, "creation_date": str(date.today()), "cart_products": [], "status": "Active"}

    with (
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

    with (
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

# ------------------- GET TESTS end -------------------


# ------------------- PUT TESTS start -------------------

def test_update_my_cart_successfully_returns_200():
    # Arrange
    user_id = 1
    cart_id = 99

    mock_cart = Cart(id=cart_id, user_id=user_id, creation_date=str(date.today()), status="Active")

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.Cart.get_by_id_obj", return_value=mock_cart) as mock_get_cart,
        patch("main.Cart.update", return_value=True) as mock_update_cart,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.put(
            f"/me/{user_id}/carts/{cart_id}",
            headers={"Authorization": "Bearer fake_token"},
            json={"status": "Abandoned"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json()["message"] == f"Cart ID {cart_id} updated successfully"
        mock_get_cart.assert_called_once_with(str(cart_id))
        mock_update_cart.assert_called_once_with(cart_products=None, status="Abandoned")
        mock_invalidate_cache.assert_called_once_with("carts", item_id=str(cart_id), identifier=str(user_id))


def test_update_my_cart_with_inexistent_cart_returns_404():
    # Arrange
    user_id = 1
    cart_id = 99

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.Cart.get_by_id_obj", return_value=None) as mock_get_cart,
        patch("main.Cart.update") as mock_update_cart,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.put(
            f"/me/{user_id}/carts/{cart_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 404
        assert response.get_json()["error_message"] == f"Cart ID {cart_id} not found"
        mock_get_cart.assert_called_once_with(str(cart_id))
        mock_update_cart.assert_not_called()
        mock_invalidate_cache.assert_not_called()


def test_update_my_cart_with_non_owner_returns_401():
    # Arrange
    user_id = 50
    cart_id = 99

    mock_cart = Cart(id=cart_id, user_id=1, creation_date=str(date.today()), status="Active")

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.Cart.get_by_id_obj", return_value=mock_cart) as mock_get_cart,
        patch("main.Cart.update") as mock_update_cart,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.put(
            f"/me/{user_id}/carts/{cart_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 401
        assert response.get_json()["error_message"] == "Invalid cart"
        mock_get_cart.assert_called_once_with(str(cart_id))
        mock_update_cart.assert_not_called()
        mock_invalidate_cache.assert_not_called()


def test_update_my_cart_with_already_completed_cart_returns_400():
    # Arrange
    user_id = 1
    cart_id = 99

    mock_cart = Cart(id=cart_id, user_id=user_id, creation_date=str(date.today()), status="Completed")

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.Cart.get_by_id_obj", return_value=mock_cart) as mock_get_cart,
        patch("main.Cart.update") as mock_update_cart,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.put(
            f"/me/{user_id}/carts/{cart_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 400
        assert response.get_json()["error_message"] == f"Cart ID {cart_id} already completed"
        mock_get_cart.assert_called_once_with(str(cart_id))
        mock_update_cart.assert_not_called()
        mock_invalidate_cache.assert_not_called()

# ------------------- PUT TESTS end -------------------


# ------------------- DELETE TESTS start -------------------

def test_delete_my_cart_successfully_returns_200():
    # Arrange
    user_id = 1
    cart_id = 99

    mock_cart = Cart(id=cart_id, user_id=user_id, creation_date=str(date.today()), status="Active")

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.Cart.get_by_id_obj", return_value=mock_cart) as mock_get_cart,
        patch("main.CartProduct.delete", return_value=True) as mock_delete_cart_products,
        patch("main.Cart.delete", return_value=True) as mock_delete_cart,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.delete(
            f"/me/{user_id}/carts/{cart_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json()["message"] == f"Cart ID {cart_id} deleted successfully"
        mock_get_cart.assert_called_once_with(str(cart_id))
        mock_delete_cart_products.assert_called_once_with(str(cart_id))
        mock_delete_cart.assert_called_once()
        mock_invalidate_cache.assert_called_once_with("carts", item_id=str(cart_id), identifier=str(user_id))


def test_delete_my_cart_with_inexistent_cart_returns_404():
    # Arrange
    user_id = 1
    cart_id = 99

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.Cart.get_by_id_obj", return_value=None) as mock_get_cart,
        patch("main.CartProduct.delete") as mock_delete_cart_products,
        patch("main.Cart.delete") as mock_delete_cart,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.delete(
            f"/me/{user_id}/carts/{cart_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 404
        assert response.get_json()["error_message"] == f"Cart ID {cart_id} not found"
        mock_get_cart.assert_called_once_with(str(cart_id))
        mock_delete_cart_products.assert_not_called()
        mock_delete_cart.assert_not_called()
        mock_invalidate_cache.assert_not_called()


def test_delete_my_cart_with_non_owner_returns_401():
    # Arrange
    user_id = 50
    cart_id = 99

    mock_cart = Cart(id=cart_id, user_id=1, creation_date=str(date.today()), status="Active")

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.Cart.get_by_id_obj", return_value=mock_cart) as mock_get_cart,
        patch("main.CartProduct.delete") as mock_delete_cart_products,
        patch("main.Cart.delete") as mock_delete_cart,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.delete(
            f"/me/{user_id}/carts/{cart_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 401
        assert response.get_json()["error_message"] == "Invalid cart"
        mock_get_cart.assert_called_once_with(str(cart_id))
        mock_delete_cart_products.assert_not_called()
        mock_delete_cart.assert_not_called()
        mock_invalidate_cache.assert_not_called()


def test_delete_my_cart_with_inactive_cart_returns_400():
    # Arrange
    user_id = 1
    cart_id = 99

    mock_cart = Cart(id=cart_id, user_id=user_id, creation_date=str(date.today()), status="Completed")

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.Cart.get_by_id_obj", return_value=mock_cart) as mock_get_cart,
        patch("main.CartProduct.delete") as mock_delete_cart_products,
        patch("main.Cart.delete") as mock_delete_cart,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.delete(
            f"/me/{user_id}/carts/{cart_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 400
        assert response.get_json()["error_message"] == "Inactive cart"
        mock_get_cart.assert_called_once_with(str(cart_id))
        mock_delete_cart_products.assert_not_called()
        mock_delete_cart.assert_not_called()
        mock_invalidate_cache.assert_not_called()