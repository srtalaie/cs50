import pytest
from jar import Jar


def test_init():
    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0
    with pytest.raises(ValueError):
        new_jar = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(12)
    assert jar.size == 12
    with pytest.raises(ValueError):
        jar.deposit(1) == "Cannot deposit more cookies than what jar's capacity allows"


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(10)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(3) == "Cannot withdraw more cookies than what is in the jar"
