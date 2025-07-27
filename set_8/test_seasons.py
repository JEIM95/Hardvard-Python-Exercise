import pytest
import seasons

def test_check_date_ok():
    assert seasons.check_date("1999-02-08") == ["1999","02","08"]

#def test_check_date_error():
    #with pytest.raises(ValueError):
        #seasons.check_date("Junio 01, 1998")
    #seasons.check_date("coche") == "Invalid date"

def test_leap_year():
    assert seasons.leap_year(1995) == "False"
    assert seasons.leap_year(2000) == "True"
    assert seasons.leap_year(2004) == "True"
    assert seasons.leap_year(1999) == "False"

def test_convert_int():
    assert seasons.convert_int(["1999","02","08"]) == [1999,2,8]
    assert seasons.convert_int(["2009","07","09"]) == [2009,7,9]