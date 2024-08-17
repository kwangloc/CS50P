from fuel import *
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_gauge():
    assert gauge(0.5) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"