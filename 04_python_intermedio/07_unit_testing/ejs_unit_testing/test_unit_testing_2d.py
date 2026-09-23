
import pytest
from unit_testing_2d import sort_string

def test_sort_string_results_in_sorted_string():
    # Arrange
    my_str = "python-variable-función-computadora-monitor"
    # Act
    result = sort_string(my_str)
    # Assert
    assert result == "computadora-función-monitor-python-variable"


def test_sort_string_with_non_string_input_raises_attribute_error():
    # Arrange
    my_str = 1234
    # Act & Assert
    with pytest.raises(AttributeError):
        sort_string(my_str)


def test_sort_string_with_empty_string():
    # Arrange
    my_str = ""
    # Act
    result = sort_string(my_str)
    # Assert
    assert result == "The string is empty."