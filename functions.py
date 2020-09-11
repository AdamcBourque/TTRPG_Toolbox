## Functions for senior project TTRPG system

from random import *

def diceRoller(diceString):
    return 0

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

roll = diceRoller("2d8+5")
