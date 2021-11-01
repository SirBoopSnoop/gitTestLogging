import leapYearFinder

checkYear = leapYearFinder.boolisLeapYear

def test_divisibility_4_Not_100():
    assert checkYear(2004) == True
    
def test_divisibility_400():
    assert checkYear(2000) == True

def test_divisibility_Not_4():
    assert checkYear(2003) == False

def test_divisibility_100_Not_400():
    assert checkYear(1900) == False
