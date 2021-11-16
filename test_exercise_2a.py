"""Zadanie 2a
Przepisz poprzednie testy tak by używać pytestowej parametryzacji, w celu usunięcia duplikacji kodu.

Podpowiedź
Chodzi o użycie dekoratora pytest.mark.parametrize."""

import pytest
from exercise_2 import odd_indexes


class TestOddIndexes:

    @pytest.mark.parametrize('value,expected', [[123456, '246'], [3456, '46']])
    def test_odd_indexes_int(self, value, expected):
        actual = odd_indexes(value)
        assert actual == expected
