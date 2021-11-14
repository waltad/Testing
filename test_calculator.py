from exercise_1 import Calc


class TestCalc:

    def setup_method(self):
        self.new_calc = Calc(4, 6)

    def test_add(self):
        actual = self.new_calc.add()
        expected = 10

        assert actual == expected

    def test_sub(self):
        actual = self.new_calc.sub()
        expected = -2

        assert actual == expected

    def test_sub_reverse(self):
        actual = self.new_calc.sub(True)
        expected = 2

        assert actual == expected

    def test_mul(self):
        actual = self.new_calc.mul()
        expected = 24

        assert actual == expected

    def test_div(self):
        actual = self.new_calc.div()
        expected = 2/3

        assert actual == expected

    def test_div_reverse(self):
        actual = self.new_calc.div(True)
        expected = 3/2

        assert actual == expected
