from exercise_2 import odd_indexes


def test_odd_indexes_int():
    value = 123456
    actual = odd_indexes(value)
    expected = '246'

    assert actual == expected
