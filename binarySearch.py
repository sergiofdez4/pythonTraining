from random import seed
from random import randint

seed()

i = 1
list = []
while i<100:
    value = randint(0, 100)
    list.append(value)
    i += 1

print("Type int value between 0 and 100")

toGuess = int(input())

list = sorted(list)

def find(l, left, right, value):
    if right >= left:
        middle = left + (right-left) // 2
        if l[middle] == value:
            return middle
        elif l[middle] > value:
            return find(l, left, middle-1, value)
        else:
            return find(l, middle+1, right, value)
    else:
        return -1
print(list)

result = find(list, 0, len(list)-1, toGuess)

if result != -1:
    print ("Index is " + str(result))
