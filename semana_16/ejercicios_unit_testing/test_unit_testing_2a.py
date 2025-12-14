
import pytest
from unit_testing_2a import sum_all_elements

def test_sum_all_elements_with_all_integers_returns_total_sum():
    # Arrange
    my_list = [4, 6, 2, 29, -6]
    # Act
    result = sum_all_elements(my_list)
    # Assert
    assert result == 35


def test_sum_all_elements_with_empty_list_returns_0():
    # Arrange
    my_list = []
    # Act
    result = sum_all_elements(my_list)
    # Assert
    assert result == 0

def test_sum_all_elements_with_non_integer_raises_value_error():
    # Arrange
    my_list = "hola"
    # Act & Assert
    with pytest.raises(ValueError):
        sum_all_elements(my_list)