import pytest

from counter.model.countable import Countable

def test_constructor1() -> None:
    assert(Countable() != None)

def test_check_positivity1():
    assert(Countable.check_positivity(0) == 1)

def test_check_positivity2():
    assert(Countable.check_positivity(-5.0) == 1)

