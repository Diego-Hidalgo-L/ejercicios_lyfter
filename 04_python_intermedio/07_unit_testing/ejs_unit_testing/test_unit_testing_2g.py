
from unit_testing_2g import return_new_list

def test_return_new_list_returns_list_of_min_len_words_correctly():
    # Arrange
    my_list = ["cielo", "sol", "maravilloso", "día"]
    min_len = 4
    # Act
    new_list = return_new_list(my_list, min_len)
    # Assert
    assert new_list == ['cielo', 'maravilloso']


def test_return_new_list_with_no_words_of_min_len_entered_returns_error_message():
    # Arrange
    my_list = ["cielo", "sol", "maravilloso", "día"]
    min_len = 12
    # Act
    new_list = return_new_list(my_list, min_len)
    # Assert
    assert new_list == "There are no words with a minimum length of 12 letters in the list you entered."


def test_return_new_list_with_empty_list_returns_error_message():
    # Arrange
    my_list = []
    min_len = 5
    # Act
    new_list = return_new_list(my_list, min_len)
    # Assert
    assert new_list == "The list is empty."