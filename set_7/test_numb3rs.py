from numb3rs import validate

def test_validate():
    assert validate("192.168.0.15") == "True"
    assert validate("1.2.3.1000") == "False"
    assert validate("cat") == "False"
    assert validate("564.564.654.524") == "False"
    assert validate("140.247.235.144") == "True"