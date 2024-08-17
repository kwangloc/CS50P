from hello import say_hello

def test_default():
    assert say_hello() == "hello, world"

    
def test_argument():
    assert say_hello("Lucas") == "hello, Lucas"