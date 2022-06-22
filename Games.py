# Choose your own adventure game with what we used
from random import randint


run = True
item = "fist"
gems = 0
health = 10.0
while (run):
    path = int(input(f'Choose a path, 1 or 2: '))
    if (path != 1 or path != 2):
        print(f'Not right! Choosing a random path for you...')
        path = randint(1,2)
    if (path == 1):
        print(f'You walk down a scary path and find a chest do you open it?')
    elif (path == 2):
        print(f'blah')