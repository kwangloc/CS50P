from numb3rs import validate

def test_validate():
    assert validate("111.222.333.444") == False
    assert validate(".222.444") == False
    assert validate("255.255.255.255") == True
