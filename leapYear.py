from random import seed
from random import randint

years = []
i = 0
seed()
while i < 10:
    years.append(randint(1, 9999))
    i += 1

print(years)

def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

bools = map(isLeapYear, years)

print(list(bools))

