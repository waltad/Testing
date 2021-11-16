import pytest
from exercise_3 import func


class TestFunc:

    @pytest.mark.parametrize("number, result", [(12, 2), (11, 2), (2, 4), (123, 26), (92, 18), (79, 14), (19023, 206)])
    def test_func(self, number, result):
        assert func(number) == result
