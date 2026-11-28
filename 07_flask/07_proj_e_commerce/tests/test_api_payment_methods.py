from main import app
from db import PaymentMethod, UserPaymentMethod

from flask import jsonify
from unittest.mock import patch


# ------------------- POST TESTS start -------------------

def test_add_payment_method_successfully_returns_201():
    # Arrange
    request_json = {"method": "Dogecoin"}
    new_payment_method = PaymentMethod(id=99, method="Dogecoin")

    with (
        patch("main.validate_admin", return_value=True),
        patch("main.PaymentMethod.add", return_value=new_payment_method) as mock_add_method,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.post(
            "/payment_methods",
            headers={"Authorization": "Bearer fake_token"},
            json=request_json
        )

        # Assert
        assert response.status_code == 201
        assert response.get_json() == {"id": 99, "method": "Dogecoin"}
        mock_add_method.assert_called_once()
        mock_invalidate_cache.assert_called_once_with("payment_methods", "all")


def test_add_payment_method_with_not_admin_returns_403():
    # Arrange
    with (
        app.app_context(),
        patch("main.validate_admin") as mock_validate_admin,
        patch("main.PaymentMethod.add") as mock_add_method,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        mock_validate_admin.return_value = (jsonify(error_message="Cannot access page"), 403)

        client = app.test_client()

        # Act
        response = client.post(
            "/payment_methods",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 403
        assert response.get_json()["error_message"] == "Cannot access page"
        mock_add_method.assert_not_called()
        mock_invalidate_cache.assert_not_called()


def test_add_my_payment_method_successfully_returns_201():
    # Arrange
    user_id = 1
    request_json = {"payment_method_id": 99, "alias": "Doge", "is_default": True}
    new_payment_method = UserPaymentMethod(id=99, user_id=user_id, payment_method_id=99, alias="Doge", is_default=True)

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.UserPaymentMethod.add", return_value=new_payment_method) as mock_add_method,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.post(
            f"/me/{user_id}/payment_methods",
            headers={"Authorization": "Bearer fake_token"},
            json=request_json
        )

        # Assert
        assert response.status_code == 201
        assert response.get_json() == {"id": 99, "user_id": user_id, "payment_method_id": 99, "alias": "Doge", "is_default": True}
        mock_add_method.assert_called_once()
        mock_invalidate_cache.assert_called_once_with("payment_methods", identifier=str(user_id))


def test_add_my_payment_method_with_unauthorized_user_returns_403():
    # Arrange
    user_id = 1

    with (
        app.app_context(),
        patch("main.validate_owner") as mock_validate_owner,
        patch("main.UserPaymentMethod.add") as mock_add_method,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        mock_validate_owner.return_value = (jsonify(error_message="Cannot access page"), 403)

        client = app.test_client()

        # Act
        response = client.post(
            f"/me/{user_id}/payment_methods",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 403
        assert response.get_json()["error_message"] == "Cannot access page"
        mock_add_method.assert_not_called()
        mock_invalidate_cache.assert_not_called()

# ------------------- POST TESTS end -------------------


# ------------------- GET TESTS start -------------------

def test_get_all_payment_methods_successfully_returns_200():
    # Arrange
    user_id = 1
    payment_method = {"payment_method_id": 99, "alias": "Doge", "is_default": True}

    with (
        patch("main.validate_user", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=None),
        patch("main.PaymentMethod.get_all", return_value=[payment_method]) as mock_get_methods,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            "/payment_methods",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json() == [{"payment_method_id": 99, "alias": "Doge", "is_default": True}]
        mock_get_methods.assert_called_once()
        mock_store_cache.assert_called_once()


def test_get_all_payment_methods_with_empty_catalog_returns_404():
    # Arrange
    user_id = 1

    with (
        patch("main.validate_user", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=None),
        patch("main.PaymentMethod.get_all", return_value=None) as mock_get_methods,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            "/payment_methods",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 404
        assert response.get_json()["error_message"] == "No payment methods found"
        mock_get_methods.assert_called_once()
        mock_store_cache.assert_not_called()


def test_get_all_payment_methods_from_cache_returns_200():
    # Arrange
    user_id = 1
    cache_result = {"payment_method_id": 99, "alias": "Doge", "is_default": True}

    with (
        patch("main.validate_user", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=[cache_result]),
        patch("main.PaymentMethod.get_all",) as mock_get_method,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/payment_methods",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json() == [{"payment_method_id": 99, "alias": "Doge", "is_default": True}]
        mock_get_method.assert_not_called()
        mock_store_cache.assert_not_called()


def test_get_my_payment_methods_successfully_returns_200():
    # Arrange
    user_id = 1
    payment_method = {"payment_method_id": 99, "alias": "Doge", "is_default": True}

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=None),
        patch("main.UserPaymentMethod.get_all_by_user_id", return_value=[payment_method]) as mock_get_methods,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}/payment_methods",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json() == [{"payment_method_id": 99, "alias": "Doge", "is_default": True}]
        mock_get_methods.assert_called_once_with(user_id)
        mock_store_cache.assert_called_once()


def test_get_my_payment_methods_from_user_with_no_payment_methods_returns_404():
    # Arrange
    user_id = 1

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=None),
        patch("main.UserPaymentMethod.get_all_by_user_id", return_value=None) as mock_get_methods,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}/payment_methods",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 404
        assert response.get_json()["error_message"] == "No payment methods found"
        mock_get_methods.assert_called_once()
        mock_store_cache.assert_not_called()

# ------------------- GET TESTS end -------------------


# ------------------- PATCH TESTS start -------------------

def test_update_user_payment_method_successfully_returns_200():
    # Arrange
    user_id = 1
    payment_method_id = 99
    payment_method = UserPaymentMethod(id=payment_method_id, user_id=user_id, payment_method_id=99, alias="Doge", is_default=True)
    request_json = {"alias": "My dogecoin account", "is_default": False}

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.UserPaymentMethod.get_by_id", return_value=payment_method) as mock_get_method,
        patch("main.UserPaymentMethod.update", return_value=True) as mock_update_method,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.patch(
            f"/me/{user_id}/payment_methods/{payment_method_id}",
            headers={"Authorization": "Bearer fake_token"},
            json=request_json
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json()["message"] == f"Payment method for user ID {user_id} updated successfully"
        mock_get_method.assert_called_once_with(str(payment_method_id))
        mock_update_method.assert_called_once_with(alias="My dogecoin account", is_default=False)
        mock_invalidate_cache.assert_called_once_with("payment_methods", item_id=str(payment_method_id), identifier=str(user_id))


def test_update_user_payment_method_with_inexistent_method_returns_404():
    # Arrange
    user_id = 1
    payment_method_id = 99
    request_json = {"alias": "My dogecoin account", "is_default": False}

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.UserPaymentMethod.get_by_id", return_value=None) as mock_get_method,
        patch("main.UserPaymentMethod.update") as mock_update_method,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.patch(
            f"/me/{user_id}/payment_methods/{payment_method_id}",
            headers={"Authorization": "Bearer fake_token"},
            json=request_json
        )

        # Assert
        assert response.status_code == 404
        assert response.get_json()["error_message"] == f"Payment method ID {payment_method_id} not found"
        mock_get_method.assert_called_once_with(str(payment_method_id))
        mock_update_method.assert_not_called()
        mock_invalidate_cache.assert_not_called()


def test_update_user_payment_method_with_unauthorized_user_returns_403():
    # Arrange
    user_id = 1
    payment_method_id = 99
    payment_method = UserPaymentMethod(id=payment_method_id, user_id=payment_method_id, payment_method_id=99, alias="Doge", is_default=True)

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.UserPaymentMethod.get_by_id", return_value=payment_method) as mock_get_method,
        patch("main.UserPaymentMethod.update") as mock_update_method,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.patch(
            f"/me/{user_id}/payment_methods/{payment_method_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 403
        assert response.get_json()["error_message"] == "Cannot access page"
        mock_get_method.assert_called_once_with(str(payment_method_id))
        mock_update_method.assert_not_called()
        mock_invalidate_cache.assert_not_called()


# ------------------- PATCH TESTS end -------------------


# ------------------- DELETE TESTS start -------------------

def test_delete_user_payment_method_successfully_returns_200():
    # Arrange
    user_id = 1
    payment_method_id = 99
    payment_method = UserPaymentMethod(id=payment_method_id, user_id=user_id, payment_method_id=99, alias="Doge", is_default=True)

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.UserPaymentMethod.get_by_id", return_value=payment_method) as mock_get_method,
        patch("main.UserPaymentMethod.delete", return_value=True) as mock_delete_method,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.delete(
            f"/me/{user_id}/payment_methods/{payment_method_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json()["message"] == f"Payment method for user ID {user_id} deleted successfully"
        mock_get_method.assert_called_once_with(str(payment_method_id))
        mock_delete_method.assert_called_once()
        mock_invalidate_cache.assert_called_once_with("payment_methods", item_id=str(payment_method_id), identifier=str(user_id))


def test_delete_user_payment_method_with_inexistent_method_returns_404():
    # Arrange
    user_id = 1
    payment_method_id = 99

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.UserPaymentMethod.get_by_id", return_value=None) as mock_get_method,
        patch("main.UserPaymentMethod.delete") as mock_delete_method,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.patch(
            f"/me/{user_id}/payment_methods/{payment_method_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 404
        assert response.get_json()["error_message"] == f"Payment method ID {payment_method_id} not found"
        mock_get_method.assert_called_once_with(str(payment_method_id))
        mock_delete_method.assert_not_called()
        mock_invalidate_cache.assert_not_called()


def test_delete_user_payment_method_with_unauthorized_user_returns_403():
    # Arrange
    user_id = 1
    payment_method_id = 99
    payment_method = UserPaymentMethod(id=payment_method_id, user_id=payment_method_id, payment_method_id=99, alias="Doge", is_default=True)

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.UserPaymentMethod.get_by_id", return_value=payment_method) as mock_get_method,
        patch("main.UserPaymentMethod.update") as mock_delete_method,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.patch(
            f"/me/{user_id}/payment_methods/{payment_method_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 403
        assert response.get_json()["error_message"] == "Cannot access page"
        mock_get_method.assert_called_once_with(str(payment_method_id))
        mock_delete_method.assert_not_called()
        mock_invalidate_cache.assert_not_called()