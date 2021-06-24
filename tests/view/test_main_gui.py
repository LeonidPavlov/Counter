import pytest

from counter.view.main_gui import App

a = App()
def test_app_exist() -> None:
    assert(a != None)

