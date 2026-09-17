
import pytest
from unittest.mock import patch, mock_open
from unit_testing_5 import read_lines

def test_read_lines_returns_expected_lines():
    # Arrange
    fake_file_content = [
    "First line\n",
    "Second line\n",
    "Third line\n"
]
    mocked_open = mock_open()
    mocked_open.return_value.readlines.return_value = fake_file_content
    # Act
    with patch("builtins.open", mocked_open):
        result = read_lines("fake/path.txt")
    # Assert
    assert result == fake_file_content


def test_read_lines_raises_file_not_found_error():
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            read_lines("non/existent/path.txt")