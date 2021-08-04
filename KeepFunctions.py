## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere
## and now Amber Kolar!!

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
def diceRoller(inputString):
    rollString = ""
    inputString = inputString.replace(" ", "")
    rollGroups = getRollGroups(inputString)

    print(rollGroups)
    return rollString

    # TODO: Input ab(cd(ef) gh(ij)) kl(mn) should get us this:
    # [
    #     ['ab', 'cd(ef) gh(ij)'],
    #     ['kl', 'mn']
    # ]
    #
    # but instead gets us this:
    # [
    #     ['ab', 'cd(ef'],
    #     ['gh', 'ij'],
    #     ['kl', 'mn']
    # ]

def getRollGroups(inputString):
    rollGroups = []
    valuesBeforeGroup = []
    recordingRollGroup = False

    for i in range(len(inputString)):
        if inputString[i] == ")":
            recordingRollGroup = False
            valuesBeforeGroup = []

        if recordingRollGroup:
            rollGroups[-1][1].append(inputString[i])
        else:
            if inputString[i] == "(":
                stringBeforeGroup = arrayToString(valuesBeforeGroup)
                numericalValuesBeforeGroup = stringBeforeGroup.split('*')[-1]
                numericalValuesBeforeGroup = split('[+-/]', numericalValuesBeforeGroup)[-1]
                rollGroups.append([numericalValuesBeforeGroup, []])
                recordingRollGroup = True
            elif inputString[i] != ")":
                valuesBeforeGroup.append(inputString[i])

    for i in range(len(rollGroups)):
        rollGroups[i][1] = arrayToString(rollGroups[i][1])

    return rollGroups

def arrayToString(arrayInput):
    stringOutput = ""
    for i in range(len(arrayInput)):
        stringOutput += arrayInput[i]
    return stringOutput

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
