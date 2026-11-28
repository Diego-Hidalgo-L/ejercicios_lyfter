from main import app
from db import Invoice, BillingAddress, UserPaymentMethod

from flask import jsonify
from unittest.mock import patch
from datetime import date


# ------------------- GET TESTS start -------------------

def test_get_my_invoices_successfully_returns_200():
    # Arrange
    user_id = 1
    # invoice = Invoice(id=99, user_id=user_id, purchase_date=date.today(), billing_address_id=99, user_payment_method_id=99, status="Completed")
    invoices = [{"id": 99, "user_id": user_id, "purchase_date": str(date.today()), "billing_address_id": 99, "user_payment_method_id": 99, "status": "Completed"}]

    with (
        patch("main.validate_owner_or_admin", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=None),
        patch("main.Invoice.get_all_by_user_id", return_value=invoices) as mock_get_invoices,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}/invoices",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json() == invoices
        mock_get_invoices.assert_called_once_with(user_id)
        mock_store_cache.assert_called_once()


def test_get_my_invoices_from_user_with_no_invoices_returns_404():
    # Arrange
    user_id = 1

    with (
        patch("main.validate_owner_or_admin", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=None),
        patch("main.Invoice.get_all_by_user_id", return_value=None) as mock_get_invoices,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}/invoices",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 404
        assert response.get_json()["error_message"] == "No invoices found"
        mock_get_invoices.assert_called_once_with(user_id)
        mock_store_cache.assert_not_called()


def test_get_my_invoices_from_unauthorized_user_returns_403():
    # Arrange
    user_id = 1

    with (
        app.app_context(),
        patch("main.validate_owner_or_admin") as mock_validation,
        patch("main.check_if_cache", return_value=None),
        patch("main.Invoice.get_all_by_user_id") as mock_get_invoices,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        mock_validation.return_value = (jsonify(error_message="Cannot access page"), 403)

        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}/invoices",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 403
        assert response.get_json()["error_message"] == "Cannot access page"
        mock_get_invoices.assert_not_called()
        mock_store_cache.assert_not_called()


def test_get_invoice_by_id_successfully_returns_200():
    # Arrange
    user_id = 1
    invoice_id = 99
    invoice = Invoice(id=invoice_id, user_id=user_id, purchase_date=str(date.today()), billing_address_id=99, user_payment_method_id=99, status="Completed")
    billing_address = BillingAddress(address="Leonida")
    user_payment_method = UserPaymentMethod(alias="My Dogecoin account")
    invoice_products = [{"id": 99, "product_id": 99, "quantity": 99, "total_price": 99}]
    formatted_invoice = {"id": invoice_id, "user_id": user_id, "purchase_date": str(date.today()), "billing_address": "Leonida", "user_payment_method": "My Dogecoin account", "products": invoice_products, "status": "Completed"}

    with (
        patch("main.Invoice.get_by_id", return_value=invoice) as mock_get_invoice,
        patch("main.validate_owner_or_admin", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=None),
        patch("main.BillingAddress.get_by_id", return_value=billing_address) as mock_get_billing,
        patch("main.UserPaymentMethod.get_by_id", return_value=user_payment_method) as mock_get_user_payment,
        patch("main.InvoiceProduct.get_by_invoice_id", return_value=invoice_products) as mock_get_products,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}/invoices/{invoice_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json() == formatted_invoice
        mock_get_invoice.assert_called_once_with(str(invoice_id))
        mock_get_billing.assert_called_once_with(invoice.billing_address_id)
        mock_get_user_payment.assert_called_once_with(invoice.user_payment_method_id)
        mock_get_products.assert_called_once_with(invoice.id)
        mock_store_cache.assert_called_once()


def test_get_invoice_by_id_with_inexistent_invoice_returns_404():
    # Arrange
    user_id = 1
    invoice_id = 99

    with (
        patch("main.Invoice.get_by_id", return_value=None) as mock_get_invoice,
        patch("main.validate_owner_or_admin"),
        patch("main.check_if_cache"),
        patch("main.BillingAddress.get_by_id") as mock_get_billing,
        patch("main.UserPaymentMethod.get_by_id") as mock_get_user_payment,
        patch("main.InvoiceProduct.get_by_invoice_id") as mock_get_products,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}/invoices/{invoice_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 404
        assert response.get_json()["error_message"] == f"Invoice ID {invoice_id} not found"
        mock_get_invoice.assert_called_once_with(str(invoice_id))
        mock_get_billing.assert_not_called()
        mock_get_user_payment.assert_not_called()
        mock_get_products.assert_not_called()
        mock_store_cache.assert_not_called()


def test_get_invoice_by_id_with_not_invoice_owner_returns_403():
    # Arrange
    user_id = 1
    invoice_id = 99
    invoice = Invoice(id=invoice_id, user_id=99, purchase_date=str(date.today()), billing_address_id=99, user_payment_method_id=99, status="Completed")

    with (
        app.app_context(),
        patch("main.Invoice.get_by_id", return_value=invoice) as mock_get_invoice,
        patch("main.validate_owner_or_admin") as mock_validation,
        patch("main.check_if_cache"),
        patch("main.BillingAddress.get_by_id") as mock_get_billing,
        patch("main.UserPaymentMethod.get_by_id") as mock_get_user_payment,
        patch("main.InvoiceProduct.get_by_invoice_id") as mock_get_products,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        mock_validation.return_value = (jsonify(error_message="Cannot access page"), 403)

        client = app.test_client()

        # Act
        response = client.get(
            f"/me/{user_id}/invoices/{invoice_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 403
        assert response.get_json()["error_message"] == "Cannot access page"
        mock_get_invoice.assert_called_once_with(str(invoice_id))
        mock_get_billing.assert_not_called()
        mock_get_user_payment.assert_not_called()
        mock_get_products.assert_not_called()
        mock_store_cache.assert_not_called()

# ------------------- GET TESTS end -------------------