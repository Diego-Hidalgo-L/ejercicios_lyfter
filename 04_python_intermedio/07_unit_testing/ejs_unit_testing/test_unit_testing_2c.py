
import pytest
from unit_testing_2c import count_letters_per_case

def test_count_letters_per_case_with_normal_str():
    # Arrange
    my_str = "I love Nación Sushi"
    # Act
    upper_case, lower_case = count_letters_per_case(my_str)
    # Assert
    assert (upper_case, lower_case) == (3, 13)


def test_count_letters_when_string_is_empty():
    # Arrange
    my_str = ""
    # Act
    upper_case, lower_case = count_letters_per_case(my_str)
    # Assert
    assert (upper_case, lower_case) == (0, 0)


def test_count_letters_when_string_is_not_string_raises_error():
    # Arrange
    my_str = 123
    # Act & Assert
    with pytest.raises(TypeError):
        count_letters_per_case(my_str)
