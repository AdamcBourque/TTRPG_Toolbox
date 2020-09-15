## Functions for senior project TTRPG system

from random import *
from tkinter import *
from re import *

def diceRoller(diceString):
    print("Rolling " + diceString + "\n")
    elems = re.split('[+-]', diceString) 
    mod = int(elems[-1])
    totalRoll = mod
    for j in range (0, len(elems)-1):
        dice = elems[j].split('d')
        for i in range (0, int(dice[0])):
            temp = randint(1, int(dice[1]))
            totalRoll += temp
            print(str(temp) + " + ", end = '')
    print(str(mod) + " = " + str(totalRoll))
    return totalRoll

## returns one item from a coma seperatied list read from a file
def selectFromFile(file):  
    text = file.read()
    items = text.split(",")
    return items[randint(0,len(items)-1)]

def turn(charSheet):
    actions = []
    bonusActions = []
    reactions = []
    spellSlots = []


    





## Test code

file = open("./testList.txt", "r")
fromFile = selectFromFile(file)
file.close()
print(fromFile)

roll = diceRoller("2d8+4d6+5")
