from main import app
from db import Product

from flask import jsonify
from unittest.mock import patch, MagicMock
from datetime import date


# ------------------- POST TESTS start -------------------

def test_add_product_successfully_returns_201():
    # Arrange
    user_id = 1
    request_json = {"name": "Dog food", "price": 10, "entry_date": str(date.today()), "stock": 10}

    with (
        patch("main.validate_admin", return_value=True),
        patch("main.Product.add", return_value=True) as mock_add_product,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.post(
            "/products",
            headers={"Authorization": "Bearer fake_token"},
            json=request_json
        )

        # Assert
        assert response.status_code == 201
        assert response.get_json()["message"] == "Product 'Dog food' added successfully"
        mock_add_product.assert_called_once()
        mock_invalidate_cache.assert_called_once()


def test_add_product_from_not_admin_returns_403():
    # Arrange
    with (
        app.app_context(),
        patch("main.validate_admin") as mock_validate_admin,
        patch("main.Product.add") as mock_add_product,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        mock_validate_admin.return_value = (jsonify(error_message="Cannot access page"), 403)
        
        client = app.test_client()

        # Act
        response = client.post(
            "/products",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 403
        assert response.get_json()["error_message"] == "Cannot access page"
        mock_add_product.assert_not_called()
        mock_invalidate_cache.assert_not_called()


def test_add_product_with_database_error_returns_500():
    # Arrange
    request_json = {"name": "Dog food", "price": 10, "entry_date": str(date.today()), "stock": 10}

    with (
        app.app_context(),
        patch("main.validate_admin", return_value=True),
        patch("main.Product.add", return_value=False) as mock_add_product,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.post(
            "/products",
            headers={"Authorization": "Bearer fake_token"},
            json=request_json
        )

        # Assert
        assert response.status_code == 500
        assert response.get_json()["error_message"] == "Error inserting product into the database"
        mock_add_product.assert_called_once()
        mock_invalidate_cache.assert_not_called()

# ------------------- POST TESTS end -------------------


# ------------------- GET TESTS start -------------------

def test_get_all_products_successfully_returns_200():
    # Arrange
    user_id = 1
    product = {"id": 1, "name": "Dog food", "price": 10, "entry_date": str(date.today()), "stock": 10}

    with (
        patch("main.validate_user", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=None),
        patch("main.Product.get_all", return_value=[product]) as mock_get_all,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            "/products",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json() == [product]
        mock_get_all.assert_called_once()
        mock_store_cache.assert_called_once()


def test_get_all_products_with_no_products_returns_404():
    # Arrange
    user_id = 1

    with (
        patch("main.validate_user", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=None),
        patch("main.Product.get_all", return_value=None) as mock_get_all,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            "/products",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 404
        assert response.get_json()["error_message"] == "No products found"
        mock_get_all.assert_called_once()
        mock_store_cache.assert_not_called()


def test_get_all_products_from_cache_returns_200():
    # Arrange
    user_id = 1
    cache_result = {"id": 1, "name": "Dog food", "price": 10, "entry_date": str(date.today()), "stock": 10}

    with (
        patch("main.validate_user", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=[cache_result]),
        patch("main.Product.get_all") as mock_get_all,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            "/products",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json() == [cache_result]
        mock_get_all.assert_not_called()
        mock_store_cache.assert_not_called()


def test_get_product_successfully_returns_200():
    # Arrange
    user_id = 1
    product_id = "1"
    product = Product(id=1, name="Dog food", price=10, entry_date=date.today(), stock=10)
    formatted_product = {"id": 1, "name": "Dog food", "price": 10, "entry_date": str(date.today()), "stock": 10}

    with (
        patch("main.validate_user", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=None),
        patch("main.Product.get_by_id", return_value=product) as mock_get_product,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/products/{product_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json() == formatted_product
        mock_get_product.assert_called_once_with(product_id)
        mock_store_cache.assert_called_once()


def test_get_product_with_inexistent_product_returns_404():
    # Arrange
    user_id = 1
    product_id = "1"

    with (
        patch("main.validate_user", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=None),
        patch("main.Product.get_by_id", return_value=None) as mock_get_product,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/products/{product_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 404
        assert response.get_json()["error_message"] == f"Product ID {product_id} not found"
        mock_get_product.assert_called_once_with(product_id)
        mock_store_cache.assert_not_called()


def test_get__product_from_cache_returns_200():
    # Arrange
    user_id = 1
    product_id = "1"
    cache_result = {"id": 1, "name": "Dog food", "price": 10, "entry_date": str(date.today()), "stock": 10}

    with (
        patch("main.validate_user", return_value=(True, {"id": user_id})),
        patch("main.check_if_cache", return_value=[cache_result]),
        patch("main.Product.get_by_id") as mock_get_product,
        patch("main.ioc.cache_manager.store_data") as mock_store_cache
    ):
        client = app.test_client()

        # Act
        response = client.get(
            f"/products/{product_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json() == [cache_result]
        mock_get_product.assert_not_called()
        mock_store_cache.assert_not_called()

# ------------------- GET TESTS start -------------------


# ------------------- PATCH TESTS start -------------------

def test_update_product_successfully_returns_200():
    # Arrange
    product_id = "1"
    product = Product(id=1, name="Dog food", price=10, entry_date=date.today(), stock=10)
    request_json = {"name": "Cat food"}

    with (
        patch("main.validate_admin", return_value=True),
        patch("main.Product.get_by_id", return_value=product) as mock_get_product,
        patch("main.Product.update", return_value=True) as mock_update_product,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.patch(
            f"/products/{product_id}",
            headers={"Authorization": "Bearer fake_token"},
            json=request_json
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json()["message"] == f"Product ID {product_id} updated successfully"
        mock_get_product.assert_called_once_with(product_id)
        mock_update_product.assert_called_once_with(name="Cat food", price=None, entry_date=None, stock=None)
        mock_invalidate_cache.assert_called_once_with("products", item_id=product_id)


def test_update_product_with_inexistent_product_returns_404():
    # Arrange
    product_id = "1"

    with (
        patch("main.validate_admin", return_value=True),
        patch("main.Product.get_by_id", return_value=None) as mock_get_product,
        patch("main.Product.update") as mock_update_product,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.patch(
            f"/products/{product_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 404
        assert response.get_json()["error_message"] == f"Product ID {product_id} not found"
        mock_get_product.assert_called_once_with(product_id)
        mock_update_product.assert_not_called()
        mock_invalidate_cache.assert_not_called()


def test_update_product_with_not_admin_returns_403():
    # Arrange
    product_id = "1"

    with (
        app.app_context(),
        patch("main.validate_admin") as mock_validate_admin,
        patch("main.Product.get_by_id") as mock_get_product,
        patch("main.Product.update") as mock_update_product,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        mock_validate_admin.return_value = (jsonify(error_message="Cannot access page"), 403)
        
        client = app.test_client()

        # Act
        response = client.patch(
            f"/products/{product_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 403
        assert response.get_json()["error_message"] == "Cannot access page"
        mock_get_product.assert_not_called()
        mock_update_product.assert_not_called()
        mock_invalidate_cache.assert_not_called()

# ------------------- PATCH TESTS start -------------------


# ------------------- DELETE TESTS start -------------------

def test_delete_product_successfully_returns_200():
    # Arrange
    product_id = "1"
    product = Product(id=1, name="Dog food", price=10, entry_date=date.today(), stock=10)

    with (
        patch("main.validate_admin", return_value=True),
        patch("main.Product.get_by_id", return_value=product) as mock_get_product,
        patch("main.Product.delete", return_value=True) as mock_delete_product,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.delete(
            f"/products/{product_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 200
        assert response.get_json()["message"] == f"Product ID {product_id} deleted successfully"
        mock_get_product.assert_called_once_with(product_id)
        mock_delete_product.assert_called_once()
        mock_invalidate_cache.assert_called_once_with("products", item_id=product_id)


def test_delete_product_with_inexistent_product_returns_404():
    # Arrange
    product_id = "1"

    with (
        patch("main.validate_admin", return_value=True),
        patch("main.Product.get_by_id", return_value=None) as mock_get_product,
        patch("main.Product.delete") as mock_update_product,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        client = app.test_client()

        # Act
        response = client.delete(
            f"/products/{product_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 404
        assert response.get_json()["error_message"] == f"Product ID {product_id} not found"
        mock_get_product.assert_called_once_with(product_id)
        mock_update_product.assert_not_called()
        mock_invalidate_cache.assert_not_called()


def test_delete_product_with_not_admin_returns_403():
    # Arrange
    product_id = "1"

    with (
        app.app_context(),
        patch("main.validate_admin") as mock_validate_admin,
        patch("main.Product.get_by_id") as mock_get_product,
        patch("main.Product.update") as mock_update_product,
        patch("main.invalidate_cache") as mock_invalidate_cache
    ):
        mock_validate_admin.return_value = (jsonify(error_message="Cannot access page"), 403)
        
        client = app.test_client()

        # Act
        response = client.delete(
            f"/products/{product_id}",
            headers={"Authorization": "Bearer fake_token"}
        )

        # Assert
        assert response.status_code == 403
        assert response.get_json()["error_message"] == "Cannot access page"
        mock_get_product.assert_not_called()
        mock_update_product.assert_not_called()
        mock_invalidate_cache.assert_not_called()