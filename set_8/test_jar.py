from jar import Jar
import pytest

def test_init():
    jar = Jar(8)
    assert jar 


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
    with pytest.raises(ValueError):
        jar.deposit(13)
        jar.deposit(15)
        jar.deposit(-8)

def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(13)
        jar.withdraw(18)
        jar.withdraw(-9)

def test_capacity():
    jar = Jar()
    assert jar.capacity == 12


def test_size():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(5)
    assert jar.size == 6
    jar.withdraw(3)
    assert jar.size == 3
    