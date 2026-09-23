
from unit_testing_2h import count_vowels

def test_count_vowels_returns_correct_amount_of_vowels():
    # Arrange
    my_str = "anthropology"
    # Act
    counter = count_vowels(my_str)
    # Assert
    assert counter == 4


def test_count_vowels_with_mixed_upper_case_and_lower_case_returns_correct_amount_of_vowels():
    # Arrange
    my_str = "ChImpanZEe"
    # Act
    counter = count_vowels(my_str)
    # Assert
    assert counter == 4


def test_count_vowels_with_non_alphabetical_string_returns_zero():
    # Arrange
    my_str = "123"
    # Act
    counter = count_vowels(my_str)
    # Assert
    assert counter == 0