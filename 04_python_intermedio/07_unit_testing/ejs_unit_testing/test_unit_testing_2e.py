
import pytest
from unit_testing_2e import check_if_prime, make_primes_list

def test_check_if_prime_with_prime_number_returns_true():
    # Arrange
    my_num = 13
    # Act
    result = check_if_prime(my_num)
    # Assert
    assert result


def test_check_if_prime_with_non_prime_number_returns_false():
    # Arrange
    my_num = 10
    # Act
    result = check_if_prime(my_num)
    # Assert
    assert not result


def test_check_if_prime_with_non_int_input_raises_type_error():
    # Arrange
    my_num = "hola"
    # Act & Assert
    with pytest.raises(TypeError):
        check_if_prime(my_num)


def test_make_primes_list_with_list_of_ints_and_or_floats_returns_list_of_only_primes():
    # Arrange
    my_list = [1, 4, 2, 5, 6, 7, 13, 9, 67, 104, 23, 41]
    # Act
    result = make_primes_list(my_list)
    # Assert
    assert result == [2, 5, 7, 13, 67, 23, 41]


def test_make_primes_list_with_non_iterable_input_raises_type_error():
    # Arrange
    my_list = 1234
    # Act & Assert
    with pytest.raises(TypeError):
        make_primes_list(my_list)


def test_make_primes_list_with_empty_list_returns_error_message():
    # Arrange
    my_list = []
    # Act
    result = make_primes_list(my_list)
    # Assert
    assert result == "The list is empty."