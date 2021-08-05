import math


def fibonacci1(index):
    if index < 2:
        return index
    return fibonacci1(index-1) + fibonacci1(index-2)

n=0
while n<10:
    print(fibonacci1(n))
    n += 1

def fibLineal(index):
    a = 0
    b = 1
    c = 0
    if index == 0:
        return a
    elif index == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

def isFibonacci(number):
    return isPerfectSquare(5 * number * number + 4) or isPerfectSquare(5 * number * number - 4)

n=0
fibonacciNumbers = []
while n<100000:
    if isFibonacci(n):
        fibonacciNumbers.append(n)
    n += 1

print(fibonacciNumbers)