from random import seed
from random import randint

print("Guess the number game");

print("Set the range of the numbers (integers)");
print("Set first number");

firstNumber = int(input());

print("Set second number");

secondNumber = int(input());

def checkNumbers(a, b):
    if a>b:
        print("Set another numbers, bye")
        exit()

checkNumbers(firstNumber, secondNumber)

seed()
toGuess = randint(firstNumber, secondNumber)

notGuessed = 1
while notGuessed:
    print("Guess the number between " + str(firstNumber) + " and " + str(secondNumber))
    guess = int(input())
    if guess>secondNumber:
        print("Its smaller than " + str(secondNumber))
        continue
    else:
        if guess<firstNumber:
            print("Its bigger than " + str(firstNumber))
            continue
    if guess == toGuess:
        print("WINNER!!!!!!!!")
        notGuessed = 0




