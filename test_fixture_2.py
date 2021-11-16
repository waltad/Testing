import pytest
from fixture_2 import Data


@pytest.fixture()
def prepared_object():
    data = Data()
    data.prepare("Kamil", "Kozak")
    yield data
    data.prepare("Kamil", "Kozak")


def test_first(prepared_object: Data):
    assert prepared_object.name == "Kamil"
    prepared_object.prepare("Kamil", "Test")
    assert prepared_object.info == "Test"


def test_second(prepared_object: Data):
    assert prepared_object.name == "Kamil"
    prepared_object.prepare("Test", "Test")
    assert prepared_object.info == "Test"
    assert prepared_object.name == "Test"
