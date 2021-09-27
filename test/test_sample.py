import pytest


def inc(x):
    return x + 1


def test_answer():
    assert inc(4) == 5


def test_fails():
    with pytest.raises(Exception) as e_info:
        assert inc(3) == 5
