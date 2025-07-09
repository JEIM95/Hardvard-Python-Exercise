import pytest
from twttr import shorten

def test_shorten():
    assert shorten("Hola") == "Hl"
    assert shorten("coche") == "cch"
    assert shorten("camionero") == "cmnr"

def test_number():
    assert shorten ("2") == "2"
    with pytest.raises(TypeError):
        shorten (5) 

def test_punctuation():
    assert shorten (".") == "."

