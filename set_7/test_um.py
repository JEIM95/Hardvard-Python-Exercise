from um import count

def test_count_alone():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("cat") == 0
    

def test_count_upper():
    assert count("Um, thanks for the album.") == 1
    


def test_count_complex():
    assert count("Um, this album is, um, really good") == 2
    assert count("Um, thanks, um...") == 2
    assert count("Um, thanks, um, regular expressions make sense now") == 2
    assert count("Um... what are regular expressions?") == 1
    assert count("Um? Mum? Is this album where, um, umm, the clumsy alums play rums?") == 2