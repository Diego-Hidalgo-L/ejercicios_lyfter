from main import app
from db import BillingAddress

from flask import jsonify
from unittest.mock import patch


# ------------------- POST TESTS start -------------------

def test_add_billing_address_successfully_returns_201():
    # Arrange
    user_id = 1
    request_json = {"address": "Leonida"}
    new_billing_address = BillingAddress(id=99, user_id=user_id, address="Leonida")

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.BillingAddress.add", return_value=new_billing_address) as mock_add_billing,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.post(
            f"/me/{user_id}/billing",
            headers={"Authorization": "Bearer fake_token"},
            json=request_json
        )

        # Assert
        assert response.status_code == 201
        assert response.get_json() == {"id": 99, "user_id": user_id, "address": "Leonida"}
        mock_add_billing.assert_called_once()
        mock_invalidate_cache.assert_called_once_with("billing_addresses", identifier=str(user_id))


def test_add_billing_address_with_unauthorized_user_returns_403():
    # Arrange
    user_id = 1

    with (
        app.app_context(),
        patch("main.validate_owner") as mock_validate_owner,
        patch("main.BillingAddress.add") as mock_add_billing,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        mock_validate_owner.return_value = (jsonify(error_message="Cannot access page"), 403)

        client = app.test_client()

        # Act
        response = client.post(
            f"/me/{user_id}/billing",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 403
        assert response.get_json()["error_message"] == "Cannot access page"
        mock_add_billing.assert_not_called()
        mock_invalidate_cache.assert_not_called()


def test_add_billing_address_with_database_error_returns_500():
    # Arrange
    user_id = 1
    request_json = {"address": "Leonida"}

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.BillingAddress.add", return_value=False) as mock_add_billing,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.post(
            f"/me/{user_id}/billing",
            headers={"Authorization": "Bearer fake_token"},
            json=request_json
        )

        # Assert
        assert response.status_code == 500
        assert response.get_json()["error_message"] == "Error adding billing address to the database"
        mock_add_billing.assert_called_once()
        mock_invalidate_cache.assert_not_called()

# ------------------- POST TESTS end -------------------


# ------------------- GET TESTS start -------------------

def test_get_one_billing_address_successfully_returns_200():
    # Arrange
    user_id = 1
    billing_id = 99
    new_billing_address = BillingAddress(id=billing_id, user_id=user_id, address="Leonida")
    formatted_billing_address = {"id": billing_id, "user_id": user_id, "address": "Leonida"}

    with (
        patch("main.validate_owner_or_admin", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=None),
        patch("main.BillingAddress.get_by_id", return_value=new_billing_address) as mock_get_billing,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}/billing/{billing_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json() == formatted_billing_address
        mock_get_billing.assert_called_once_with(str(billing_id))
        mock_store_cache.assert_called_once()


def test_get_one_billing_address_with_user_with_no_billing_addresses_returns_404():
    # Arrange
    user_id = 1
    billing_id = 99

    with (
        patch("main.validate_owner_or_admin", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=None),
        patch("main.BillingAddress.get_by_id", return_value=None) as mock_get_billing,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}/billing/{billing_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 404
        assert response.get_json()["error_message"] == "No billing addresses found"
        mock_get_billing.assert_called_once_with(str(billing_id))
        mock_store_cache.assert_not_called()


def test_get_one_billing_address_from_cache_returns_200():
    # Arrange
    user_id = 1
    billing_id = 99
    cache_result = {"id": billing_id, "user_id": user_id, "address": "Leonida"}

    with (
        patch("main.validate_owner_or_admin", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=cache_result),
        patch("main.BillingAddress.get_by_id") as mock_get_billing,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}/billing/{billing_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json() == cache_result
        mock_get_billing.assert_not_called()
        mock_store_cache.assert_not_called()


def test_get_my_billing_addresses_for_user_with_addresses_returns_200():
    # Arrange
    user_id = 1
    my_billing_addresses = [{"id": 99, "user_id": user_id, "address": "Leonida"}]

    with (
        patch("main.validate_owner_or_admin", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=None),
        patch("main.BillingAddress.get_all_by_user_id", return_value=my_billing_addresses) as mock_get_billing,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}/billing",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json() == my_billing_addresses
        mock_get_billing.assert_called_once_with(user_id)
        mock_store_cache.assert_called_once()


def test_get_my_billing_addresses_for_user_with_no_addresses_returns_404():
    # Arrange
    user_id = 1

    with (
        patch("main.validate_owner_or_admin", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=None),
        patch("main.BillingAddress.get_all_by_user_id", return_value=None) as mock_get_billing,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}/billing",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 404
        assert response.get_json()["error_message"] == "No billing addresses found"
        mock_get_billing.assert_called_once()
        mock_store_cache.assert_not_called()


def test_get_my_billing_addresses_for_unauthorized_user_returns_403():
    # Arrange
    user_id = 1

    with (
        app.app_context(),
        patch("main.validate_owner_or_admin") as mock_validation,
        patch("main.check_if_cache"),
        patch("main.BillingAddress.get_all_by_user_id") as mock_get_billing,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        mock_validation.return_value = (jsonify(error_message="Cannot access page"), 403)
    
        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}/billing",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 403
        assert response.get_json()["error_message"] == "Cannot access page"
        mock_get_billing.assert_not_called()
        mock_store_cache.assert_not_called()

# ------------------- GET TESTS end -------------------


# ------------------- PATCH TESTS start -------------------

def test_update_billing_address_successfully_returns_200():
    # Arrange
    user_id = 1
    billing_id = 99
    billing_address = BillingAddress(id=billing_id, user_id=user_id, address="Leonida")
    request_json = {"address": "Hyrule"}

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.BillingAddress.get_by_id", return_value=billing_address) as mock_get_billing,
        patch("main.BillingAddress.update", return_value=True) as mock_update_billing,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.patch(
            f"/me/{user_id}/billing/{billing_id}",
            headers={"Authorization": "Bearer fake_token"},
            json=request_json
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json()["message"] == f"Billing address for user ID {user_id} updated successfully"
        mock_get_billing.assert_called_once_with(str(billing_id))
        mock_update_billing.assert_called_once_with("Hyrule")
        mock_invalidate_cache.assert_called_once_with("billing_addresses", item_id=str(billing_id), identifier=str(user_id))


def test_update_billing_address_with_inexistent_address_returns_404():
    # Arrange
    user_id = 1
    billing_id = 99
    request_json = {"address": "Hyrule"}

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.BillingAddress.get_by_id", return_value=None) as mock_get_billing,
        patch("main.BillingAddress.update") as mock_update_billing,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.patch(
            f"/me/{user_id}/billing/{billing_id}",
            headers={"Authorization": "Bearer fake_token"},
            json=request_json
        )

        # Assert
        assert response.status_code == 404
        assert response.get_json()["error_message"] == "No billing addresses found"
        mock_get_billing.assert_called_once_with(str(billing_id))
        mock_update_billing.assert_not_called()
        mock_invalidate_cache.assert_not_called()


def test_update_billing_address_with_unauthorized_user_returns_404():
    # Arrange
    user_id = 1
    billing_id = 99
    request_json = {"address": "Hyrule"}

    with (
        app.app_context(),
        patch("main.validate_owner") as mock_validation,
        patch("main.BillingAddress.get_by_id") as mock_get_billing,
        patch("main.BillingAddress.update") as mock_update_billing,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        mock_validation.return_value = (jsonify(error_message="Cannot access page"), 403)
    
        client = app.test_client()

        # Act
        response = client.patch(
            f"/me/{user_id}/billing/{billing_id}",
            headers={"Authorization": "Bearer fake_token"},
            json=request_json
        )

        # Assert
        assert response.status_code == 403
        assert response.get_json()["error_message"] == "Cannot access page"
        mock_get_billing.assert_not_called()
        mock_update_billing.assert_not_called()
        mock_invalidate_cache.assert_not_called()

# ------------------- PATCH TESTS end -------------------


# ------------------- DELETE TESTS start -------------------

def test_delete_billing_address_successfully_returns_200():
    # Arrange
    user_id = 1
    billing_id = 99
    billing_address = BillingAddress(id=billing_id, user_id=user_id, address="Leonida")

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.BillingAddress.get_by_id", return_value=billing_address) as mock_get_billing,
        patch("main.BillingAddress.delete", return_value=True) as mock_delete_billing,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.delete(
            f"/me/{user_id}/billing/{billing_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json()["message"] == f"Billing address for user ID {user_id} deleted successfully"
        mock_get_billing.assert_called_once_with(str(billing_id))
        mock_delete_billing.assert_called_once()
        mock_invalidate_cache.assert_called_once_with("billing_addresses", item_id=str(billing_id), identifier=str(user_id))


def test_delete_billing_address_with_inexistent_address_returns_404():
    # Arrange
    user_id = 1
    billing_id = 99

    with (
        patch("main.validate_owner", return_value=(True, {"id": user_id})),
        patch("main.BillingAddress.get_by_id", return_value=None) as mock_get_billing,
        patch("main.BillingAddress.delete", return_value=True) as mock_delete_billing,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.delete(
            f"/me/{user_id}/billing/{billing_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 404
        assert response.get_json()["error_message"] == f"Billing address ID {user_id} not found"
        mock_get_billing.assert_called_once_with(str(billing_id))
        mock_delete_billing.assert_not_called()
        mock_invalidate_cache.assert_not_called()


def test_update_billing_address_with_unauthorized_user_returns_404():
    # Arrange
    user_id = 1
    billing_id = 99

    with (
        app.app_context(),
        patch("main.validate_owner") as mock_validation,
        patch("main.BillingAddress.get_by_id") as mock_get_billing,
        patch("main.BillingAddress.delete") as mock_delete_billing,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        mock_validation.return_value = (jsonify(error_message="Cannot access page"), 403)
    
        client = app.test_client()

        # Act
        response = client.delete(
            f"/me/{user_id}/billing/{billing_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 403
        assert response.get_json()["error_message"] == "Cannot access page"
        mock_get_billing.assert_not_called()
        mock_delete_billing.assert_not_called()
        mock_invalidate_cache.assert_not_called()

# ------------------- DELETE TESTS end -------------------