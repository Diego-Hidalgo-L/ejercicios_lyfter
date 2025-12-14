
from math_utilities import sum_list_items

def test_sum_list_items_with_small_numbers_sums_all_items_correctly():
    # AAA
    # Arrange
    items_list = [3, 7, 8]
    #Act
    result = sum_list_items(items_list)
    # Assert
    assert result == 18


def test_sum_list_items_with_big_numbers_sums_all_items_correctly():
    # AAA
    # Arrange
    items_list = [3333, 79898, 83411]
    # Act
    result = sum_list_items(items_list)
    # Assert
    assert result == 166642
