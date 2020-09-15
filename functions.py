## Functions for senior project TTRPG system

from random import *  ## for pseudorandom number generation
from tkinter import * ## for GUI support
from re import *      ## for re.split


## dice roller function takes a string "2d8+5" and prints the rolls and total.
## returns total as an int
def diceRoller(diceString):
    print("Rolling " + diceString + "\n")
    elems = re.split('[+-]', diceString) ##splits into dice types and mod
    mod = int(elems[-1]) ## stat modifier 
    totalRoll = mod
    for j in range (0, len(elems)-1):
        dice = elems[j].split('d') ## seperates dice quantity and sizes
        for i in range (0, int(dice[0])):
            temp = randint(1, int(dice[1])) 
            totalRoll += temp ## adds each dice roll to the total
            print(str(temp) + " + ", end = '') ## prints each roll
    print(str(mod) + " = " + str(totalRoll)) ## prints total
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
