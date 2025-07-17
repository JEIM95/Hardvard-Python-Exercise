import pytest
import fuel

def test_gauge():
    assert fuel.convert("3/4") == 75
    assert fuel.convert("1/4") == 25
    assert fuel.convert("4/4") == 100
    assert fuel.convert("0/4") == 0
    
    with pytest.raises(ValueError):
        fuel.convert("5.5/7.6")
        fuel.convert("8/4")
        fuel.convert("-5/7")
        fuel.convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("7/0")

def test_letter():
    assert fuel.gauge(75) == "75%"
    assert fuel.gauge(25) == "25%"
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(1) == "E"