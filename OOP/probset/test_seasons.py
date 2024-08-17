import pytest
from seasons import count_minutes

def test_valid_input():
    assert count_minutes("2022-07-21") == "Five hundred twenty-five thousand, six hundred minutes"

def test_invalid_input():
    with pytest.raises(ValueError):
        count_minutes("meow meow")
