import pytest
import project

def test_Check_reading_values():
    assert project.Check_reading_values("Full") == True
    assert project.Check_reading_values("2025-09-07") == True

    with pytest.raises(SystemExit):
        assert project.Check_reading_values("hola")
    with pytest.raises(SystemExit):
        assert project.Check_reading_values("01-09-1995")

def test_Check_date():
    assert project.Check_date("2029-08-05") == True
    assert project.Check_date("1752-07-63") == True

    with pytest.raises(SystemExit):
        assert project.Check_date("Hola")
    with pytest.raises(SystemExit):
        assert project.Check_date("01-09-1995")

def test_Check_writing_values():
    assert project.Check_writing_values("-c","-v","500") == True

    with pytest.raises(SystemExit):
        assert project.Check_writing_values("-k","-q","900")
    with pytest.raises(SystemExit):
        assert project.Check_writing_values("-c","-v","hola")
