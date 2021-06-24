import pytest
from counter.aux.error_handling import ACHTUNG

ah = ACHTUNG(RuntimeError(), __file__, 'test_init()')

def test_init() -> None:
    assert(ah != None)

def test_console() -> None:
    assert(ah.console() == None)
