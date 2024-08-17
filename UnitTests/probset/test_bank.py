from bank import value

def test_hello_lower():
    assert value("hello") == 0

def test_hello_upper():
    assert value("HELLO") == 0

def test_start_w_h():
    assert value("hey Lucas") == 20
    assert value("hi Lucas") == 20

def test_no_greeting():
    assert value("good morning, Lucas") == 100
    assert value("what's up Lucas") == 100

