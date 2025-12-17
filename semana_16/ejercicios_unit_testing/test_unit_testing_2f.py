
from unit_testing_2f import count_chars

def test_count_chars_with_all_lower_case_string_returns_correct_amount_of_target_letter():
    # Arrange
    my_str = "aesthetic"
    target_letter = "e"
    # Act
    result_str, result_letter, counter = count_chars(my_str, target_letter)
    # Assert
    assert result_str == "aesthetic"
    assert result_letter == "e"
    assert counter == 2


def test_count_chars_with_mixed_upper_case_and_lower_case_returns_correct_amount_of_target_letter():
    # Arrange
    my_str = "AmAzOnIa"
    target_letter = "A"
    # Act
    result_str, result_letter, counter = count_chars(my_str, target_letter)
    # Assert
    assert result_str == "amazonia"
    assert result_letter == "a"
    assert counter == 3


def test_count_chars_with_all_upper_case_returns_correct_amount_of_target_letter():
    # Arrange
    my_str = "WATERWAY"
    target_letter = "w"
    # Act
    result_str, result_letter, counter = count_chars(my_str, target_letter)
    # Assert
    assert result_str == "waterway"
    assert result_letter == "w"
    assert counter == 2