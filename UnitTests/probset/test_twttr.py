from twttr import shorten

def test_upper():
    assert shorten("HELLO") == "HLL"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("LUCAS") == "LCS"

def test_lower():
    assert shorten("hello") == "hll"
    assert shorten("twitter") == "twttr"
    assert shorten("lucas") == "lcs"

def test_number():
    assert shorten("CS50") == "CS50"
    assert shorten("Cub50") == "Cb50"

def test_punctuation():
    assert shorten("Hello.") == "Hll."
