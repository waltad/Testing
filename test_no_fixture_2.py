from unittest import TestCase
from fixture_2 import Data


class Test(TestCase):

    def setUp(self):
        self.data = Data()
        self.data.prepare("Kamil", "Kozak")

    def test_first(self):
        assert self.data.name == "Kamil"
        self.data.prepare("Kamil", "Test")
        assert self.data.info == "Test"

    def test_second(self):
        assert self.data.name == "Kamil"
        self.data.prepare("Test", "Test")
        assert self.data.info == "Test"
        assert self.data.name == "Test"

    def tearDown(self):
        self.data.prepare("Kamil", "Kozak")
