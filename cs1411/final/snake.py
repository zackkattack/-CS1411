import time
import os
from random import randint

x = 40
y = 30
playerX = int(x/2)
playerY = int(y/2)
foodX = randint(1,x)
foodY = randint(1,y)

# def moveUp():
#     return playerY+=1

def KeyInput():
    while True:
        key = input(":")
        if key == 'a':
            playerX -= 1
            break
        if key == 'd':
            playerX += 1
            break
        if key == 's':
            playerY -= 1
            break
        if key == 'w':
            playerY += 1
            break

def draw():
    for i in range(0,x):
        print("#", end='')

    print("")

    for i in range(0,y):
        for j in range(0,x):
            if j == 0:
                print("#", end='')
            if i == playerY and j == playerY:
                print("O", end="")
            elif i == foodY and j == foodX-2:
                print("F", end="")
            else:
                print(" ", end='')

            if j == x-2:
                print("#", end="")

        print()

    for i in range(0,x):
        print("#", end="")

#

#os.system('clear')

while(True):
    os.system("clear")
    draw()
    KeyInput()
    time.sleep(1)
