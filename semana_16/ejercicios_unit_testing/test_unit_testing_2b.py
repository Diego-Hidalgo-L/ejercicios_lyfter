
import pytest
from unit_testing_2b import invert_string

def test_invert_string_when_string_is_ok_returns_string_inverted_properly():
    # Arrange
    my_str = "Hola mundo"
    # Act
    result = invert_string(my_str)
    # Assert
    assert result == "odnum aloH"


def test_invert_string_when_string_is_empty_returns_error_message():
    # Arrange
    my_str = ""
    # Act
    result = invert_string(my_str)
    # Assert
    assert result == "The string is empty."


def test_invert_string_when_input_not_a_string_raises_type_error():
    # Arrange
    my_str = 145
    # Act
    with pytest.raises(TypeError):
        invert_string(my_str)