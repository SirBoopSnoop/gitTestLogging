
def isDivisibleBy_4_Not_100(year):
    if ((year%4 == 0 and year%100 != 0) and year < 4000):
        return True
    else: return False

def isDivisibleBy_400(year):
    if (year%400 == 0 and year < 4000):
        return True
    else: return False

def notDivisibleBy_4(year):
    if (year%4 != 0):
        return True
    else: return False

def isDivisibleBy_100_Not_400(year):
    if (year%100 == 0 and year%400 != 0):
        return True
    else: return False

def boolisLeapYear(year):

    if (isDivisibleBy_4_Not_100(year) or isDivisibleBy_400(year)):
        return True

    elif (notDivisibleBy_4(year) or isDivisibleBy_100_Not_400(year)):
        return False

    else:
        print("Calendar is 2418 years old and it's time for an update")
    
    
        
