import pytest
from bank import value

def test_letters():
    assert value("Hello") == "$0"
    assert value("Good Morining") == "$100"
    assert value("hola") == "$20"
    assert value("hola, esto es una prueba") == "$20"

def test_number():
    with pytest.raises(AttributeError):
        value(4)
        value(-333)
        value(0)