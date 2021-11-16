from unittest.mock import MagicMock, patch

from mock_example_2 import AvgCalculator


def test_calculate_avg():
    data = [['1', '2', '3', '4', '5'], ['2', '4', '1', '12']]
    mock = MagicMock(return_value=data)

    with patch('mock_example_2.AvgCalculator._get_content', mock):
        avg_calc = AvgCalculator('fake.txt')
        assert avg_calc.calculate() == [3.0, 4.75]


def test_get_raw_data():
    data = [['1', '2', '3', '4', '5'], ['2', '4', '1', '12']]
    mock = MagicMock(return_value=data)

    with patch('mock_example_2.AvgCalculator._get_content', mock):
        avg_calc = AvgCalculator('fake.txt')
        assert avg_calc.get_data() == data