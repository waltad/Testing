from pytest import fixture, mark
from exercise_5 import Product, Warehouse


@fixture
def products():
    return [Product("name1", 24.30), Product("name2", 42), Product("name3", 75.98)]


@mark.parametrize("capacity, result", [(100, -1), (142.28, 0), (150, 7.72)])
def test_warehouses(capacity, result, products):
    w = Warehouse(capacity)
    last_result = None
    for product in products:
        last_result = w.add(product)

    assert round(last_result, 2) == result
