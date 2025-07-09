import pytest
from twttr import shorten

def test_shorten():
    assert shorten("Hola") == "Hl"
    assert shorten("coche") == "cch"
    assert shorten("camionero") == "cmnr"

