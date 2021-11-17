from unittest.mock import patch, MagicMock
from exercise_4 import _get_data, get_avg


def test_func():
    _get_data_mock = MagicMock(return_value='123456789')

    with patch('test_exercise_4._get_data', _get_data_mock):
        assert get_avg(3) == 2
        assert get_avg(1) == 1
        assert get_avg(2) == 1.5
