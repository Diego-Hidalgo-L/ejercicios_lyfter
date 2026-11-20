from db import Cart, CartProduct

from unittest.mock import MagicMock, patch, call
from datetime import date


# ------------------- GET METHODS start -------------------

def test_get_or_create_active_cart_with_already_active_cart_returns_active_cart():
    # Arrange
    user_id = 1

    mock_cart = MagicMock(user_id=user_id, status="Active")

    with patch("db.Session") as mock_session_class:
        mock_session = mock_session_class.return_value.__enter__.return_value
        mock_session.scalar.return_value = mock_cart

        # Act
        result = Cart.get_or_create_active_cart(user_id)

        # Assert
        assert result is mock_cart
        assert mock_cart.status == "Active"
        mock_session.scalar.assert_called_once()
        mock_session.add.assert_not_called()
        mock_session.commit.assert_not_called()


def test_get_or_create_active_cart_without_active_cart_creates_and_returns_new_active_cart():
    # Arrange
    user_id = 1

    with patch("db.Session") as mock_session_class:
        mock_session = mock_session_class.return_value.__enter__.return_value
        mock_session.scalar.return_value = None

        # Act
        result = Cart.get_or_create_active_cart(user_id)

        # Assert
        assert isinstance(result, Cart)
        assert result.user_id == user_id
        assert result.status == "Active"
        mock_session.scalar.assert_called_once()
        mock_session.add.assert_called_once_with(result)
        mock_session.commit.assert_called_once()
        mock_session.refresh.assert_called_once_with(result)


def test_get_or_create_active_cart_with_database_error_returns_500():
    # Arrange
    user_id = 1

    with patch("db.Session") as mock_session_class:
        mock_session = mock_session_class.return_value.__enter__.return_value
        mock_session.scalar.side_effect = Exception("Database error")

        # Act
        result = Cart.get_or_create_active_cart(user_id)

        # Assert
        assert result is False
        mock_session.scalar.assert_called_once()
        mock_session.add.assert_not_called()
        mock_session.commit.assert_not_called()
        mock_session.refresh.assert_not_called()
        mock_session.rollback.assert_called_once()


def test_get_by_id_dict_with_existing_products_returns_cart_in_dictionary_form():
    # Arrange
    cart_id = 1
    creation_date = date.today()

    cart_product = CartProduct(cart_id=cart_id, product_id=3, quantity=5, total_price=25)
    cart = Cart(id=cart_id, user_id=1, creation_date=creation_date, status="Active")
    cart.cart_products = [cart_product]

    with patch("db.Session") as mock_session_class:
        mock_session = mock_session_class.return_value.__enter__.return_value
        mock_session.get.return_value = cart

        # Act
        result = Cart.get_by_id_dict(cart_id)

        # Assert
        assert result == {"id": 1, "user_id": 1, "creation_date": creation_date, "cart_products":[{"product_id": 3, "quantity": 5, "total_price": 25}], "status": "Active"}
        mock_session.get.assert_called_once_with(Cart, cart_id)


def test_get_by_id_dict_with_inexistent_cart_returns_none():
    # Arrange
    cart_id = 1
    cart = None

    with patch("db.Session") as mock_session_class:
        mock_session = mock_session_class.return_value.__enter__.return_value
        mock_session.get.return_value = cart

        # Act
        result = Cart.get_by_id_dict(cart_id)

        # Assert
        assert result == None
        mock_session.get.assert_called_once_with(Cart, cart_id)


def test_get_all_by_user_id_and_user_has_carts_returns_list_of_cart_dictionaries():
    # Arrange
    user_id = 1
    creation_date = date.today()

    cart_a_id = 1
    cart_a_product = CartProduct(cart_id=cart_a_id, product_id=3, quantity=5, total_price=25)
    cart_a = Cart(id=cart_a_id, user_id=user_id, creation_date=creation_date, status="Completed")
    # cart_a.cart_products = [cart_a_product] -> no necesito asignar esto, porque get_all_by_user_id() obtiene los productos mediante CartProduct.get_by_cart_id()

    cart_b_id = 2
    cart_b_product = CartProduct(cart_id=cart_b_id, product_id=7, quantity=2, total_price=14)
    cart_b = Cart(id=cart_b_id, user_id=user_id, creation_date=creation_date, status="Active")
    # cart_b.cart_products = [cart_b_product] -> no necesito asignar esto, porque get_all_by_user_id() obtiene los productos mediante CartProduct.get_by_cart_id()

    carts = [cart_a, cart_b]

    with (
        patch("db.Session") as mock_session_class,
        patch("db.CartProduct.get_by_cart_id", side_effect=[
            [cart_a_product.format_dict()],
            [cart_b_product.format_dict()]
        ]) as mock_get_products
    ):
        mock_session = mock_session_class.return_value.__enter__.return_value
        mock_session.scalars.return_value.all.return_value = carts

        # Act
        result = Cart.get_all_by_user_id(user_id)

        # Assert
        assert result == [
            {
                "id": cart_a_id,
                "user_id": user_id,
                "creation_date": creation_date,
                "cart_products": [
                    {
                        "product_id": 3,
                        "quantity": 5,
                        "total_price": 25
                    }
                ],
                "status": "Completed"
            },
            {
                "id": cart_b_id,
                "user_id": user_id,
                "creation_date": creation_date,
                "cart_products": [
                    {
                        "product_id": 7,
                        "quantity": 2,
                        "total_price": 14
                    }
                ],
                "status": "Active"
            }
        ]
        mock_session.scalars.assert_called_once()
        assert mock_get_products.call_count == 2
        mock_get_products.assert_has_calls([
            call(cart_a_id),
            call(cart_b_id)
        ])


def test_get_all_by_user_id_when_user_has_no_carts_returns_none():
    # Arrange
    user_id = 1
    carts = None

    with patch("db.Session") as mock_session_class:
        mock_session = mock_session_class.return_value.__enter__.return_value
        mock_session_class.scalars.return_value = carts

        # Act
        result = Cart.get_all_by_user_id(user_id)

        # Assert
        assert result == []
        mock_session.scalars.assert_called_once()

# ------------------- GET METHODS end -------------------


# ------------------- UPDATE start -------------------

def test_update_cart_products_only_returns_true():
    # Arrange
    cart = Cart(id=1, user_id=2, status="Active")

    mock_cart_product = [{"product_id": 1, "quantity": 5, "total_price": 10}]
    mock_cart = MagicMock(id=1, user_id=2, status="Active")

    with patch("db.Session") as mock_session_class:
        mock_session = mock_session_class.return_value.__enter__.return_value
        mock_session.get.return_value = mock_cart

        # Act
        result = cart.update(cart_products=mock_cart_product)

        # Assert
        assert result is True
        mock_session.get.assert_called_once_with(Cart, cart.id)
        mock_session.execute.assert_called_once()
        mock_session.add.assert_called_once()
        mock_session.commit.assert_called_once()

        added_product = mock_session.add.call_args.args[0]

        assert isinstance(added_product, CartProduct)
        assert added_product.cart_id == 1
        assert added_product.product_id == 1
        assert added_product.quantity == 5
        assert added_product.total_price == 10


def test_update_status_only_returns_true():
    # Arrange
    cart = Cart(id=1, user_id=2, status="Active")
    mock_cart = MagicMock(id=1, user_id=2, status="Active")

    with patch("db.Session") as mock_session_class:
        mock_session = mock_session_class.return_value.__enter__.return_value
        mock_session.get.return_value = mock_cart

        # Act
        result = cart.update(status="Abandoned")

        # Assert
        assert result is True
        assert mock_cart.status == "Abandoned"
        mock_session.get.assert_called_once_with(Cart, cart.id)
        mock_session.execute.assert_not_called()
        mock_session.add.assert_not_called()
        mock_session.commit.assert_called_once()


def test_update_both_cart_products_and_status_returns_true():
    # Arrange
    cart = Cart(id=1, user_id=2, status="Active")

    mock_cart_product = [{"product_id": 1, "quantity": 5, "total_price": 10}]
    mock_cart = MagicMock(id=1, user_id=2, status="Active")

    with patch("db.Session") as mock_session_class:
        mock_session = mock_session_class.return_value.__enter__.return_value
        mock_session.get.return_value = mock_cart

        # Act
        result = cart.update(cart_products=mock_cart_product, status="Abandoned")

        # Assert
        assert result is True
        assert mock_cart.status == "Abandoned"
        mock_session.get.assert_called_once_with(Cart, cart.id)
        mock_session.execute.assert_called_once()
        mock_session.add.assert_called_once()
        mock_session.commit.assert_called_once()

        added_product = mock_session.add.call_args.args[0]

        assert isinstance(added_product, CartProduct)
        assert added_product.cart_id == 1
        assert added_product.product_id == 1
        assert added_product.quantity == 5
        assert added_product.total_price == 10


def test_update_with_database_error_returns_false():
    # Arrange
    cart = Cart(id=1, user_id=2, status="Active")

    with patch("db.Session") as mock_session_class:
        mock_session = mock_session_class.return_value.__enter__.return_value
        mock_session.get.side_effect = Exception("Database error")

        # Act
        result = cart.update()

        # Assert
        assert result is False
        mock_session.get.assert_called_once()
        mock_session.execute.assert_not_called()
        mock_session.add.assert_not_called()
        mock_session.commit.assert_not_called()
        mock_session.rollback.assert_called_once()

# ------------------- UPDATE end -------------------


# ------------------- DELETE start -------------------

def test_delete_existing_cart_returns_true():
    # Arrange
    cart = Cart(id=5, user_id=5, status="Abandoned")
    mock_cart = MagicMock(id=5, user_id=5, status="Abandoned")

    with patch("db.Session") as mock_session_class:
        mock_session = mock_session_class.return_value.__enter__.return_value
        mock_session.get.return_value = mock_cart

        # Act
        result = cart.delete()

        # Assert
        assert result == True
        mock_session.delete.assert_called_once_with(mock_cart)
        mock_session.commit.assert_called_once()


def test_delete_cart_with_database_error_returns_false():
    # Arrange
    cart = Cart(id=5)

    with patch("db.Session") as mock_session_class:
        mock_session = mock_session_class.return_value.__enter__.return_value
        mock_session.get.side_effect = Exception("Database error")

        # Act
        result = cart.delete()

        # Assert
        assert result == False
        mock_session.delete.assert_not_called()
        mock_session.commit.assert_not_called()
        mock_session.rollback.assert_called_once()


def test_delete_cart_products_returns_true():
    # Arrange
    cart_id = 5

    with patch("db.Session") as mock_session_class:
        mock_session = mock_session_class.return_value.__enter__.return_value

        # Act
        result = CartProduct.delete(cart_id)

        # Assert
        assert result == True
        mock_session.execute.assert_called_once()
        mock_session.commit.assert_called_once()

