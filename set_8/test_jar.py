from jar import Jar
import pytest

def test_init():
    jar = Jar(5)
    assert jar.capacity == 5
    


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(4)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(5)
    assert jar.size == 6

    with pytest.raises(ValueError):
        jar.deposit(7)
    with pytest.raises(ValueError):    
        jar.deposit(15)
    with pytest.raises(ValueError):
        jar.deposit(-8)

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(3)
    with pytest.raises(ValueError):
        jar.withdraw(18)
    with pytest.raises(ValueError):
        jar.withdraw(-9)

def test_capacity():
    with pytest.raises(ValueError):
        jar = Jar(-5)

    