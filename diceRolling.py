from random import seed
from random import randint

seed()
stop = 1

while stop:
    value = randint(1, 6)
    print("Type 'r' to roll the dice")
    print("Type 's' to stop")
    rollAgain = input()
    if rollAgain == "r":
        print("DICE VALUE: "+ str(value) +"\n")
        continue
    else:
        if rollAgain == "s":
            exit()