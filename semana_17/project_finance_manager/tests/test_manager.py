
import pytest
from semana_17.project_finance_manager.project.manager import FinanceManager

# test add_category()
def test_adding_valid_category():
    # Arrange
    manager = FinanceManager()
    category = "Work"
    # Act
    result = manager.add_category(category)
    # Assert
    assert result == "'Work' added to Categories"


def test_adding_duplicate_category():
    # Arrange
    manager = FinanceManager()
    manager.add_category("Work")
    new_category = "Work"
    # Act & Assert
    with pytest.raises(ValueError):
        manager.add_category(new_category)


def test_adding_empty_category():
    # Arrange
    manager = FinanceManager()
    category = ""
    # Act & Assert
    with pytest.raises(ValueError):
        manager.add_category(category)


# test add_income()
def test_adding_valid_income():
    # Arrange
    manager = FinanceManager()
    manager.add_category("Work")
    # Act
    result = manager.add_income("Salary", 1500, "Work")
    # Assert
    assert result == "Income registered"


def test_adding_negative_income():
    # Arrange
    manager = FinanceManager()
    manager.add_category("Misc")
    # Act & Assert
    with pytest.raises(ValueError):
        manager.add_income("Extra hours", -250, "Misc")


def test_adding_income_with_invalid_category():
    # Arrange
    manager = FinanceManager()
    manager.add_category("Work")
    manager.add_category("Freelance")
    manager.add_category("Food")
    manager.add_category("Transportation")
    manager.add_category("Fun")
    manager.add_category("Misc")
    # Act & Assert
    with pytest.raises(ValueError):
        manager.add_income("Extra hours", 250, "Extra")


# test add_expense()
def test_adding_valid_expense():
    # Arrange
    manager = FinanceManager()
    manager.add_category("Food")
    # Act
    result = manager.add_expense("Lunch", 25, "Food")
    # Assert
    assert result == "Expense registered"


def test_adding_negative_expense():
    # Arrange
    manager = FinanceManager()
    manager.add_category("Food")
    # Act & Assert
    with pytest.raises(ValueError):
        manager.add_expense("Lunch", -25, "Food")


def test_adding_expense_with_invalid_category():
    # Arrange
    manager = FinanceManager()
    manager.add_category("Work")
    manager.add_category("Freelance")
    manager.add_category("Food")
    manager.add_category("Transportation")
    manager.add_category("Fun")
    manager.add_category("Misc")
    # Act & Assert
    with pytest.raises(ValueError):
        manager.add_expense("Laundry", 15, "Extra")


# test get_total_income()
def test_get_total_income():
    # Arrange
    manager = FinanceManager()
    # Create categories
    manager.add_category("Work")
    manager.add_category("Food")
    manager.add_category("Misc")
    manager.add_category("Freelance")
        # Create movements
    manager.add_income("Salary", 1500, "Work")
    manager.add_income("Extra hours", 250, "Work")
    manager.add_expense("Lunch", 18, "Food")
    manager.add_expense("Gym membership", 90, "Misc")
    manager.add_income("Photo shoot", 300, "Freelance")
    # Act
    result = manager.get_total_income()
    # Assert
    assert result == 2050


# test get_total_expense()
def test_get_total_expense():
    # Arrange
    manager = FinanceManager()
        # Create categories
    manager.add_category("Work")
    manager.add_category("Food")
    manager.add_category("Misc")
    manager.add_category("Freelance")
        # Create movements
    manager.add_income("Salary", 1500, "Work")
    manager.add_income("Extra hours", 250, "Work")
    manager.add_expense("Lunch", 18, "Food")
    manager.add_expense("Gym membership", 90, "Misc")
    manager.add_income("Photo shoot", 300, "Freelance")
    # Act
    result = manager.get_total_expense()
    # Assert
    assert result == 108


# test_get_balance()
def test_get_balance():
    # Arrange
    manager = FinanceManager()
        # Create categories
    manager.add_category("Work")
    manager.add_category("Food")
    manager.add_category("Misc")
    manager.add_category("Freelance")
        # Create movements
    manager.add_income("Salary", 1500, "Work")
    manager.add_income("Extra hours", 250, "Work")
    manager.add_expense("Lunch", 18, "Food")
    manager.add_expense("Gym membership", 90, "Misc")
    manager.add_income("Photo shoot", 300, "Freelance")
    # Act
    result = manager.get_balance()
    # Assert
    assert result == 1942


# test category_exists()
def test_category_exists():
    # Arrange
    manager = FinanceManager()
    # Act
    manager.add_category("Food")
    result = manager.category_exists("Food")
    # Assert
    assert result == True