import pytest


@pytest.fixture()
def my_fixture():
    print("\n I'm the fixture - setUp")
    yield
    print("I'm the fixture - tearDown")


def test_first(my_fixture):
    print("I'm the first test")
