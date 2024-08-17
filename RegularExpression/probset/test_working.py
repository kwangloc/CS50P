import pytest
from working import convert

def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")

def test_wrong_minute():
    with pytest.raises(ValueError):
        convert("13:60 AM to 5 PM")

def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_to():
    with pytest.raises(ValueError):
        convert("13 AM 5 PM")

def test_format():
    with pytest.raises(ValueError):
        convert("13 AM - 5 PM")