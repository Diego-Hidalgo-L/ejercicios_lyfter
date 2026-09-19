import pytest
from unit_testing_1 import bubble_sort

def test_bubble_sort_with_short_list_results_in_sorted_list_three_iterations_and_eight_swaps():
    # Arrange
    list_to_sort = [19, 78, -3, 81, 34, 35, 67]
    # Act
    iterations, swaps = bubble_sort(list_to_sort)
    # Assert
    assert (iterations, swaps) == (3, 8)
    assert list_to_sort == [-3, 19, 34, 35, 67, 78, 81]


def test_bubble_sort_with_list_of_100_plus_elements_results_in_sorted_list():
    # Assert
    long_list = [59, 9, 71, 94, 21, 26, 80, 68, 83, 13, 27, 7, 4, 53, 84, 38, 51, 69, 7, 68, 31, 20, 84, 67, 27, 9, 48, 61, 98, 85, 99, 32, 97, 50, 50, 99, 87, 41, 96, 51, 89, 52, 98, 11, 31, 67, 19, 91, 5, 95, 57, 58, 62, 13, 2, 51, 44, 90, 12, 43, 29, 88, 66, 21, 4, 40, 35, 48, 68, 62, 10, 21, 99, 12, 19, 91, 61, 26, 18, 48, 1, 29, 92, 59, 62, 79, 96, 66, 69, 15, 18, 93, 9, 2, 36, 69, 3, 98, 10, 38, 86]
    # Act
    iterations, swaps = bubble_sort(long_list)
    # Assert
    assert (iterations, swaps) == (94, 2604)
    assert long_list == sorted(long_list)


def test_bubble_sort_with_empty_list_returns_none_none():
    # Assert
    empty_list = []
    # Act
    result = bubble_sort(empty_list)
    # Assert
    assert result == (None, None)


def test_bubble_sort_with_non_list_object_raises_value_error():
    # Assert
    my_string = "hola"
    # Act & Assert
    with pytest.raises(ValueError):
        bubble_sort(my_string)