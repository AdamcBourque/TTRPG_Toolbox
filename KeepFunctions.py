## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere

from tkinter import *
from tkinter import font as tkFont
from re import split      ## for re.split weird 3.9
from random import *  ## for pseudorandom number generation
from tkinter import filedialog
from Spell import *
from Weapon import *
from os import listdir
from math import *



##----------------------------------------------------------------------------------------------------------------------------------
##   Global Variables
##----------------------------------------------------------------------------------------------------------------------------------


BgColor = "grey19"
lblColor = "grey35"

##fontColor = "pink"

##----------------------------------------------------------------------------------------------------------------------------------
##   Global Functions                               
##----------------------------------------------------------------------------------------------------------------------------------

## dice roller function takes a string "2d8+5" and prints the rolls and total.
## returns total as an int
def diceRoller(diceString):

    diceString = diceString.replace(' ', '')
    elems = split('[+-]', diceString) ##splits into dice types and mod
    test = split('[1234567890d]', diceString)
    totalRoll = ""
    total = 0
    gross = True
    while (gross == True):
        try:
            test.remove('')
        except ValueError:
           gross = False
    
    opString = diceString
    for i in elems:
        opString = opString.replace(i,'')
    
    
    for j in range (0, len(elems)-1):
        dice = elems[j].split('d') ## seperates dice quantity and sizes
        try:
            num = int(dice[0])
        except ValueError:
            num = 1
        if (num > 200):
            return "I don't have that many dice to roll"
        for i in range (0, num):
            temp = randint(1, int(dice[1])) 
            
            if (num - i == 1):    ## test if last dice in group
                if (test == []):
                    totalRoll += str(temp)
                    total += temp ## adds each dice roll to the total
                else:
                    totalRoll += (str(temp) + test[j])
                    if (j == 0): ## test if first group
                        total += temp ## adds each dice roll to the total
                    else:
                        if (test[j-1] == '+'):
                            total += temp ## adds each dice roll to the total
                        else:
                            total -= temp ## subtracts each dice roll to the total
            else:
                total += temp ## adds each dice roll to the total
                totalRoll += (str(temp) + "+")
                
    if (elems[-1].find('d') == -1): ## Checks if there is a modifier
        mod = elems[-1] ## stat modifier
        if (test[-1] == '+'):
            total += int(mod)
        else:
            total -= int(mod)
        totalRoll += str(mod)
    else:
        dice = elems[-1].split('d') ## seperates dice quantity and sizes
        try:
            num = int(dice[0])
        except ValueError:
            num = 1
        for i in range (0, num):
            temp = randint(1, int(dice[1])) 
            total += temp ## adds each dice roll to the total
            if (num - i == 1):
                totalRoll += str(temp)
            else:
                totalRoll += (str(temp) + "+")
        
        
    totalRoll += (" = " + str(total))

    return totalRoll
               

def readCSV(filename):  ## makes a list from a csv
    file = open(filename, "r", encoding="utf8")
    text = file.read()
    file.close()
    items = text.split(",")
    items[0] = items[0].replace("ï»¿", '') ## remove garbage from front of string
    items[-1] = items[-1].replace("\n", '') ## remove garbage from back of string
    return items

def readTupleCSV(filename):
    file = open(filename, "r", encoding="utf-8-sig")
    text = file.read()
    file.close()
    items = text.split("),")
    items[0] = items[0].replace("ï»¿", '') ## remove garbage from front of string
    items[-1] = items[-1].replace("\n", '') ## remove garbage from back of string
    tuples = []
    for i in items:
        i = i.replace("(", '')
        i = i.replace(")", '')
        temp = i.split(',')
        tuples.append(temp)
    return tuples

def readTupleCSV2(filename):
    file = open(filename, "r", encoding="utf-8-sig")
    text = file.read()
    file.close()
    items = text.split("),")
    items[0] = items[0].replace("ï»¿", '') ## remove garbage from front of string
    items[-1] = items[-1].replace("\n", '') ## remove garbage from back of string
    return items


## returns one item from a coma seperatied list
def selectFromList(items):  
    return items[randint(0,len(items)-1)]


def gcd(a, b):
    t=0
    while (b!=0):
    	t=b
    	b=a%b
    	a=t	
    return a

def reduce(numerator,denominator):
    fac = gcd(numerator,denominator)
    numerator /= fac
    denominator /= fac
    return [numerator,denominator]

def dec_to_frac(num):
    dec_part = num % 1
    if (dec_part != 0):
        numerator = dec_part
        denominator = 1
        while(numerator % 1 != 0):
            numerator *= 10
            denominator *= 10
        temp = reduce(numerator,denominator)
        if ((num - dec_part) != 0):
            return str(int(num - dec_part)) + " " + str(int(temp[0])) + '/' + str(int(temp[1]))
        else:
            return str(int(temp[0])) + '/' + str(int(temp[1]))
    else:
        return str(int(num))
    
def file_error():
    error = Toplevel(self)
    error.title("Notice")
    error.geometry("400x200")
    error.iconbitmap(r"The-Keep.ico")

    error.config(background=BgColor)

    label = Label(error, fg="white smoke", background=BgColor, text = "No File Selected")
    label.pack()
