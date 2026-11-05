from services import Transaction
from db import Cart

from unittest.mock import MagicMock, patch
import pytest

# ------------------- PURCHASE start -------------------

def test_purchase_with_valid_billing_info_and_cart_id_returns_true():
    # Arrange
    user_id = 1
    cart_id = 2
    billing_address_id = 1
    user_payment_method_id = 2

    mock_cart_product = MagicMock(product_id=10, quantity=2, total_price=5000)
    mock_cart = MagicMock(user_id=user_id, status="Active", cart_products=[mock_cart_product])
    mock_billing_address = MagicMock(user_id=user_id)
    mock_payment_method = MagicMock(user_id=user_id)
    mock_product = MagicMock(stock=10)

    with (
        patch("services.Session") as mock_session_class,
        patch("services.BillingAddress.get_by_id", return_value=mock_billing_address),
        patch("services.UserPaymentMethod.get_by_id", return_value=mock_payment_method),
        patch("services.invalidate_cache"),
    ):
        mock_session = mock_session_class.return_value.__enter__.return_value

        mock_session.get.side_effect = lambda model, identifier: {
            ("Cart", cart_id): mock_cart,
            ("Product", mock_cart_product.product_id): mock_product,
        }.get((model.__name__, identifier))

        # Act
        result = Transaction().purchase(user_id, cart_id, billing_address_id, user_payment_method_id)

        # Assert
        assert result == (True, 201)
        assert mock_product.stock == 8
        assert mock_cart.status == "Completed"
        mock_session.commit.assert_called_once()


def test_purchase_with_inexistent_cart_returns_not_found():
    # Arrange
    user_id = 1
    cart_id = 3
    billing_address_id = 1
    user_payment_method_id = 1

    with patch("services.Session") as mock_session_class:
        mock_session = mock_session_class.return_value.__enter__.return_value
        mock_session.get.return_value = None

        # Act
        result = Transaction().purchase(user_id, cart_id, billing_address_id, user_payment_method_id)

        # Assert
        assert result == ("Cart not found", 404)
        mock_session.commit.assert_not_called()


def test_purchase_with_not_cart_owner_returns_invalid():
    # Arrange
    user_id = 2
    cart_id = 3
    billing_address_id = 4
    user_payment_method_id = 5

    mock_cart = MagicMock(user_id=3)

    with patch("services.Session") as mock_session_class:
        mock_session = mock_session_class.return_value.__enter__.return_value
        mock_session.get.return_value = mock_cart

        # Act
        result = Transaction().purchase(user_id, cart_id, billing_address_id, user_payment_method_id)

        # Assert
        assert result == ("Invalid cart", 401)
        mock_session.get.assert_called_once_with(Cart, cart_id)
        mock_session.commit.assert_not_called()


def test_purchase_with_inactive_cart_returns_inactive():
    # Arrange
    user_id = 2
    cart_id = 3
    billing_address_id = 4
    user_payment_method_id = 5

    mock_cart = MagicMock(user_id=user_id, status='Abandoned')

    with patch("services.Session") as mock_session_class:
        mock_session = mock_session_class.return_value.__enter__.return_value
        mock_session.get.return_value = mock_cart

        # Act
        result = Transaction().purchase(user_id, cart_id, billing_address_id, user_payment_method_id)

        # Assert
        assert result == ("Inactive cart", 400)
        mock_session.get.assert_called_once_with(Cart, cart_id)
        mock_session.commit.assert_not_called()


def test_purchase_with_inexistent_billing_address_returns_not_found():
    # Arrange
    user_id = 2
    cart_id = 3
    billing_address_id = 4
    user_payment_method_id = 5

    mock_cart = MagicMock(user_id=user_id, status='Active')

    with (
        patch("services.Session") as mock_session_class,
        patch("services.BillingAddress.get_by_id", return_value=None)
    ):
        mock_session = mock_session_class.return_value.__enter__.return_value
        mock_session.get.return_value = mock_cart

        # Act
        result = Transaction().purchase(user_id, cart_id, billing_address_id, user_payment_method_id)

        # Assert
        assert result == ("Billing address not found", 404)
        mock_session.get.assert_called_once_with(Cart, cart_id)
        mock_session.commit.assert_not_called()


def test_purchase_with_not_billing_address_owner_returns_invalid():
    # Arrange
    user_id = 2
    cart_id = 3
    billing_address_id = 4
    user_payment_method_id = 5

    mock_cart = MagicMock(user_id=user_id, status='Active')
    mock_billing_address = MagicMock(user_id=1)

    with (
        patch("services.Session") as mock_session_class,
        patch("services.BillingAddress.get_by_id", return_value=mock_billing_address)
    ):
        mock_session = mock_session_class.return_value.__enter__.return_value
        mock_session.get.return_value = mock_cart

        # Act
        result = Transaction().purchase(user_id, cart_id, billing_address_id, user_payment_method_id)

        # Assert
        assert result == ("Invalid billing address", 401)
        mock_session.get.assert_called_once_with(Cart, cart_id)
        mock_session.commit.assert_not_called()


def test_purchase_with_inexistent_payment_method_returns_not_found():
    # Arrange
    user_id = 2
    cart_id = 3
    billing_address_id = 4
    user_payment_method_id = 5

    mock_cart = MagicMock(user_id=user_id, status='Active')
    mock_billing_address = MagicMock(user_id=user_id)

    with (
        patch("services.Session") as mock_session_class,
        patch("services.BillingAddress.get_by_id", return_value=mock_billing_address),
        patch("services.UserPaymentMethod.get_by_id", return_value=None)
    ):
        mock_session = mock_session_class.return_value.__enter__.return_value
        mock_session.get.return_value = mock_cart

        # Act
        result = Transaction().purchase(user_id, cart_id, billing_address_id, user_payment_method_id)

        # Assert
        assert result == ("User payment method not found", 404)
        mock_session.get.assert_called_once_with(Cart, cart_id)
        mock_session.commit.assert_not_called()


def test_purchase_with_not_payment_method_owner_returns_invalid():
    # Arrange
    user_id = 2
    cart_id = 3
    billing_address_id = 4
    user_payment_method_id = 5

    mock_cart = MagicMock(user_id=user_id, status='Active')
    mock_billing_address = MagicMock(user_id=user_id)
    mock_payment_method = MagicMock(user_id=1)

    with (
        patch("services.Session") as mock_session_class,
        patch("services.BillingAddress.get_by_id", return_value=mock_billing_address),
        patch("services.UserPaymentMethod.get_by_id", return_value=mock_payment_method)
    ):
        mock_session = mock_session_class.return_value.__enter__.return_value
        mock_session.get.return_value = mock_cart

        # Act
        result = Transaction().purchase(user_id, cart_id, billing_address_id, user_payment_method_id)

        # Assert
        assert result == ("Invalid user payment method", 401)
        mock_session.get.assert_called_once_with(Cart, cart_id)
        mock_session.commit.assert_not_called()


def test_purchase_with_inexistent_product_returns_not_found():
    # Arrange
    user_id = 2
    cart_id = 3
    billing_address_id = 4
    user_payment_method_id = 5

    mock_cart_product = MagicMock(product_id=10)
    mock_cart = MagicMock(user_id=user_id, status='Active', cart_products=[mock_cart_product])
    mock_billing_address = MagicMock(user_id=user_id)
    mock_payment_method = MagicMock(user_id=user_id)

    with (
        patch("services.Session") as mock_session_class,
        patch("services.BillingAddress.get_by_id", return_value=mock_billing_address),
        patch("services.UserPaymentMethod.get_by_id", return_value=mock_payment_method)
    ):
        mock_session = mock_session_class.return_value.__enter__.return_value

        mock_session.get.side_effect = lambda model, identifier: {
            ("Cart", cart_id): mock_cart,
            ("Product", mock_cart_product.product_id): None,
        }.get((model.__name__, identifier))

        # Act
        result = Transaction().purchase(user_id, cart_id, billing_address_id, user_payment_method_id)

        # Assert
        assert result == (f"Product ID {mock_cart_product.product_id} not found", 404)
        assert mock_session.get.call_count == 2
        mock_session.add.assert_not_called()
        mock_session.commit.assert_not_called()


def test_purchase_with_insufficient_stock_returns_insufficient():
    # Arrange
    user_id = 2
    cart_id = 3
    billing_address_id = 4
    user_payment_method_id = 5

    mock_cart_product = MagicMock(product_id=10, quantity=8) # total_price=5000
    mock_cart = MagicMock(user_id=user_id, status='Active', cart_products=[mock_cart_product])
    mock_billing_address = MagicMock(user_id=user_id)
    mock_payment_method = MagicMock(user_id=user_id)
    mock_product = MagicMock(stock=2)

    with (
        patch("services.Session") as mock_session_class,
        patch("services.BillingAddress.get_by_id", return_value=mock_billing_address),
        patch("services.UserPaymentMethod.get_by_id", return_value=mock_payment_method)
    ):
        mock_session = mock_session_class.return_value.__enter__.return_value

        mock_session.get.side_effect = lambda model, identifier: {
            ("Cart", cart_id): mock_cart,
            ("Product", 10): mock_product,
        }.get((model.__name__, identifier))

        # Act
        result = Transaction().purchase(user_id, cart_id, billing_address_id, user_payment_method_id)

        # Assert
        assert result == (f"Insufficient stock for product ID {mock_cart_product.product_id} (Desired purchase quantity: {mock_cart_product.quantity} - Available stock: {mock_product.stock}).", 400)
        assert mock_session.get.call_count == 2
        mock_session.add.assert_not_called()
        mock_session.commit.assert_not_called()


def test_purchase_with_database_error_returns_error():
    # Arrange
    user_id = 2
    cart_id = 3
    billing_address_id = 4
    user_payment_method_id = 5

    with patch("services.Session") as mock_session_class:
        mock_session = mock_session_class.return_value.__enter__.return_value

        mock_session.get.side_effect = Exception("Database connection error")

        # Act
        result = Transaction().purchase(user_id, cart_id, billing_address_id, user_payment_method_id)

        # Assert
        assert result == ("Error adding purchase to the database: Database connection error", 500)
        mock_session.rollback.assert_called_once()
        mock_session.commit.assert_not_called()

# ------------------- PURCHASE end -------------------