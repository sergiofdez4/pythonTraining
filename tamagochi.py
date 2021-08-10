import random
from random import seed
from random import randrange
import string

seed()

class Pet():

    hunger_max = 10
    boredom_max = 10
    hunger_decrement = 1
    boredom_decrement = 1

    sounds = ["".join((random.choice(string.ascii_letters) for _ in range(10)))]

    def __init__(self, name = "Tamagochi"):
        self.name = name
        self.hunger = randrange(self.hunger_max)
        self.boredom = randrange(self.boredom_max)
        self.sounds = self.sounds[:]

    def clock_tick(self):
        self.hunger += 1
        self.boredom += 1

    def state(self):
        if self.boredom >= self.boredom_max:
            return "bored"
        elif self.hunger <= self.hunger_max and self.boredom <= self.boredom_max:
            return "happy"
        else:
            return "hungry"

    def __str__(self):
        result = "PET: Name: --{} Mood: --{}".format(self.name, self.state())
        return result

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def feed(self):
        self.reduce_hunger()


tamako = Pet("Tamako")
print(tamako)

for i in range(10):
    tamako.clock_tick()
    print(tamako.__str__())

for i in range(10):
    tamako.feed()

tamako.teach("friend")

for i in range(10):
    tamako.feed()
    print(tamako.__str__())
