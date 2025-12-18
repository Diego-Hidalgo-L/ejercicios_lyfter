
import unittest
from unit_testing_3 import add, average, convert_celsius_to_fahrenheit

class TestAdd(unittest.TestCase):
    def test_add_with_positive_numbers(self):
        # Arrange
        number1 = 4
        number2 = 8
        # Act
        result  = add(number1, number2)
        # Assert
        self.assertEqual(result, 12)

    def test_add_with_negative_numbers(self):
        # Arrange
        number1 = -12
        number2 = -5
        # Act
        result  = add(number1, number2)
        # Assert
        self.assertEqual(result, -17)
    
    def test_add_with_zero(self):
        # Arrange
        number1 = 0
        number2 = 8
        # Act
        result  = add(number1, number2)
        # Assert
        self.assertEqual(result, 8)


class TestAverage(unittest.TestCase):
    def test_average_with_positive_numbers(self):
        # Arrange
        list_of_args = [1, 3, 5, 7]
        # Act
        result = average(list_of_args)
        # Assert
        self.assertEqual(result, 4.0)
    
    def test_average_with_negative_numbers(self):
        # Arrange
        list_of_args = [-1, -3, -5, -7]
        # Act
        result = average(list_of_args)
        # Assert
        self.assertEqual(result, -4.0)
    
    def test_average_with_zero(self):
        # Arrange
        list_of_args = [13, 6, 0, 24, 0, 51]
        # Act
        result = average(list_of_args)
        # Assert
        self.assertEqual(result, 15.67)


class TestConvertCelsiusToFahrenheit(unittest.TestCase):
    def test_convert_celsius_to_fahrenheit_with_positive_numbers(self):
        # Arrange
        celsius = 25
        # Act
        fahrenheit = convert_celsius_to_fahrenheit(celsius)
        # Assert
        self.assertEqual(fahrenheit, 77.0)

    def test_convert_celsius_to_fahrenheit_with_negative_numbers(self):
        # Arrange
        celsius = -12
        # Act
        fahrenheit = convert_celsius_to_fahrenheit(celsius)
        # Assert
        self.assertEqual(fahrenheit, 10.4)

    def test_convert_celsius_to_fahrenheit_with_zero(self):
        # Arrange
        celsius = 0
        # Act
        fahrenheit = convert_celsius_to_fahrenheit(celsius)
        # Assert
        self.assertEqual(fahrenheit, 32.0)


if __name__ == "__main__":
    unittest.main()