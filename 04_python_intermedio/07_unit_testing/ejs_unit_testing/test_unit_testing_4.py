
import pytest
from unit_testing_4 import divide

def test_divide_with_two_integers_divides_correctly():
    # Arrange
    number_1 = 10
    number_2 = 2
    # Act
    result = divide(number_1, number_2)
    # Assert
    assert result == 5.0


def test_divide_when_dividing_by_zero_raises_value_error():
    # Arrange
    number_1 = 6
    number_2 = 0
    # Act & Assert
    with pytest.raises(ValueError):
        divide(number_1, number_2)


def test_divide_when_giving_string_input_raises_type_error():
    # Arrange
    number_1 = "hola"
    number_2 = 5
    # Act & Assert
    with pytest.raises(TypeError):
        divide(number_1, number_2)