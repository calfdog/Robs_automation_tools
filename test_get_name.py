import name_gen
import pytest


def test_get_name():
    """tests the get_name function"""
    name = name_gen.get_name()
    print(name)
    assert len(name) > 0

test_get_name()


