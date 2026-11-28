from main import app
from db import Invoice

# from flask import jsonify
from unittest.mock import patch
from datetime import date


# ------------------- PURCHASE TESTS start -------------------

def test_make_purchase_successfully_returns_201():
    # Arrange
    cart_id = 99
    request_json = {"billing_address_id": 99, "user_payment_method_id": 99}

    with (
        patch("main.validate_user", return_value=(True, {"id": 1})),
        patch("main.Transaction.purchase", return_value=(True, 201)) as mock_purchase
    ):
        client = app.test_client()

        # Act
        response = client.post(
            f"/checkout/{cart_id}",
            headers={"Authorization": "Bearer fake_token"},
            json=request_json
        )

        # Assert
        assert response.status_code == 201
        assert response.get_json()["message"] == "Purchase successful"
        mock_purchase.assert_called_once_with(1, str(cart_id), 99, 99)


def test_make_purchase_with_inexistent_cart_returns_404():
    # Arrange
    cart_id = 99
    request_json = {"billing_address_id": 99, "user_payment_method_id": 99}

    with (
        patch("main.validate_user", return_value=(True, {"id": 1})),
        patch("main.Transaction.purchase", return_value=("Cart not found", 404)) as mock_purchase
    ):
        client = app.test_client()

        # Act
        response = client.post(
            f"/checkout/{cart_id}",
            headers={"Authorization": "Bearer fake_token"},
            json=request_json
        )

        # Assert
        assert response.status_code == 404
        assert response.get_json()["error_message"] == "Cart not found"
        mock_purchase.assert_called_once_with(1, str(cart_id), 99, 99)


def test_make_purchase_with_not_cart_owner_returns_401():
    # Arrange
    cart_id = 99
    request_json = {"billing_address_id": 99, "user_payment_method_id": 99}

    with (
        patch("main.validate_user", return_value=(True, {"id": 1})),
        patch("main.Transaction.purchase", return_value=("Invalid cart", 401)) as mock_purchase
    ):
        client = app.test_client()

        # Act
        response = client.post(
            f"/checkout/{cart_id}",
            headers={"Authorization": "Bearer fake_token"},
            json=request_json
        )

        # Assert
        assert response.status_code == 401
        assert response.get_json()["error_message"] == "Invalid cart"
        mock_purchase.assert_called_once_with(1, str(cart_id), 99, 99)


def test_make_purchase_with_insufficient_stock_returns_400():
    # Arrange
    cart_id = 99
    request_json = {"billing_address_id": 99, "user_payment_method_id": 99}
    product_id = 99
    purchase_quantity = 99
    available_stock = 1

    with (
        patch("main.validate_user", return_value=(True, {"id": 1})),
        patch("main.Transaction.purchase", return_value=(f"Insufficient stock for product ID {product_id} (Desired purchase quantity: {purchase_quantity} - Available stock: {available_stock})", 400)) as mock_purchase
    ):
        client = app.test_client()

        # Act
        response = client.post(
            f"/checkout/{cart_id}",
            headers={"Authorization": "Bearer fake_token"},
            json=request_json
        )

        # Assert
        assert response.status_code == 400
        assert response.get_json()["error_message"] == f"Insufficient stock for product ID {product_id} (Desired purchase quantity: {purchase_quantity} - Available stock: {available_stock})"
        mock_purchase.assert_called_once_with(1, str(cart_id), 99, 99)


def test_make_purchase_with_unexpected_error_returns_500():
    # Arrange
    cart_id = 99
    request_json = {"billing_address_id": 99, "user_payment_method_id": 99}
    error = "Commit error"

    with (
        patch("main.validate_user", return_value=(True, {"id": 1})),
        patch("main.Transaction.purchase", return_value=(f"Error adding purchase to the database: {error}", 500)) as mock_purchase
    ):
        client = app.test_client()

        # Act
        response = client.post(
            f"/checkout/{cart_id}",
            headers={"Authorization": "Bearer fake_token"},
            json=request_json
        )

        # Assert
        assert response.status_code == 500
        assert response.get_json()["error_message"] == f"Error adding purchase to the database: {error}"
        mock_purchase.assert_called_once_with(1, str(cart_id), 99, 99)

# ------------------- PURCHASE TESTS end -------------------


# ------------------- RETURN TESTS start -------------------

def test_return_purchase_successfully_returns_200():
    # Arrange
    user_id = 1
    invoice_id = 99
    invoice = Invoice(id=invoice_id, user_id=user_id, purchase_date=str(date.today()), billing_address_id=99, user_payment_method_id=99, status="Completed")

    with (
        patch("main.Invoice.get_by_id", return_value=invoice) as mock_get_invoice,
        patch("main.validate_owner_or_admin", return_value=(True, {"id": user_id})) as mock_validation,
        patch("main.Transaction.return_purchase", return_value=(True, 200)) as mock_return
    ):
        client = app.test_client()

        # Act
        response = client.post(
            f"/return/{invoice_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json()["message"] == "Purchase returned successfully"
        mock_get_invoice.assert_called_once_with(str(invoice_id))
        mock_validation.assert_called_once()
        mock_return.assert_called_once_with(str(invoice_id), user_id)


def test_return_purchase_with_not_invoice_owner_returns_401():
    # Arrange
    user_id = 1
    invoice_id = 99
    invoice = Invoice(id=invoice_id, user_id=user_id, purchase_date=str(date.today()), billing_address_id=99, user_payment_method_id=99, status="Completed")

    with (
        patch("main.Invoice.get_by_id", return_value=invoice) as mock_get_invoice,
        patch("main.validate_owner_or_admin", return_value=(True, {"id": user_id})) as mock_validation,
        patch("main.Transaction.return_purchase", return_value=("Invalid invoice", 401)) as mock_return
    ):
        client = app.test_client()

        # Act
        response = client.post(
            f"/return/{invoice_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 401
        assert response.get_json()["error_message"] == "Invalid invoice"
        mock_get_invoice.assert_called_once_with(str(invoice_id))
        mock_validation.assert_called_once()
        mock_return.assert_called_once_with(str(invoice_id), user_id)


def test_return_purchase_with_already_returned_invoice_returns_400():
    # Arrange
    user_id = 1
    invoice_id = 99
    invoice = Invoice(id=invoice_id, user_id=user_id, purchase_date=str(date.today()), billing_address_id=99, user_payment_method_id=99, status="Completed")

    with (
        patch("main.Invoice.get_by_id", return_value=invoice) as mock_get_invoice,
        patch("main.validate_owner_or_admin", return_value=(True, {"id": user_id})) as mock_validation,
        patch("main.Transaction.return_purchase", return_value=("Invoice already returned", 400)) as mock_return
    ):
        client = app.test_client()

        # Act
        response = client.post(
            f"/return/{invoice_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 400
        assert response.get_json()["error_message"] == "Invoice already returned"
        mock_get_invoice.assert_called_once_with(str(invoice_id))
        mock_validation.assert_called_once()
        mock_return.assert_called_once_with(str(invoice_id), user_id)


def test_return_purchase_with_inexistent_invoice_returns_404():
    # Arrange
    invoice_id = 99

    with (
        patch("main.Invoice.get_by_id", return_value=None) as mock_get_invoice,
        patch("main.validate_owner_or_admin") as mock_validation,
        patch("main.Transaction.return_purchase") as mock_return
    ):
        client = app.test_client()

        # Act
        response = client.post(
            f"/return/{invoice_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 404
        assert response.get_json()["error_message"] == f"Invoice ID {invoice_id} not found"
        mock_get_invoice.assert_called_once_with(str(invoice_id))
        mock_validation.assert_not_called()
        mock_return.assert_not_called()


def test_return_purchase_with_unexpected_error_returns_500():
    # Arrange
    user_id = 1
    invoice_id = 99
    invoice = Invoice(id=invoice_id, user_id=user_id, purchase_date=str(date.today()), billing_address_id=99, user_payment_method_id=99, status="Completed")
    error = "Commit error"

    with (
        patch("main.Invoice.get_by_id", return_value=invoice) as mock_get_invoice,
        patch("main.validate_owner_or_admin", return_value=(True, {"id": user_id})) as mock_validation,
        patch("main.Transaction.return_purchase", return_value=(f"Error returning invoice in the database: {error}", 500)) as mock_return
    ):
        client = app.test_client()

        # Act
        response = client.post(
            f"/return/{invoice_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 500
        assert response.get_json()["error_message"] == f"Error returning invoice in the database: {error}"
        mock_get_invoice.assert_called_once_with(str(invoice_id))
        mock_validation.assert_called_once()
        mock_return.assert_called_once_with(str(invoice_id), user_id)

# ------------------- RETURN TESTS end -------------------