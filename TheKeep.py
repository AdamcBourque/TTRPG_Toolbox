## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere

from tkinter import *
from tkinter import font as tkFont
from re import split      ## for re.split
from random import *  ## for pseudorandom number generation


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
    
    elems = re.split('[+-]', diceString) ##splits into dice types and mod
    test = re.split('[1234567890d]', diceString)
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
    return items

def readTupleCSV(filename):
    file = open(filename, "r", encoding="utf8")
    text = file.read()
    file.close()
    items = text.split("),")
    items[0] = items[0].replace("ï»¿", '') ## remove garbage from front of string
    tuples = []
    for i in items:
        i = i.replace("(", '')
        i = i.replace(")", '')
        temp = i.split(',')
        tuples.append(temp)
    return tuples

## returns one item from a coma seperatied list
def selectFromList(items):  
    return items[randint(0,len(items)-1)]

##----------------------------------------------------------------------------------------------------------------------------------
##   Individual Tools 
##----------------------------------------------------------------------------------------------------------------------------------

## These classes will be the other tool GUI's
class NpcGen(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("NPC Generator") 
        self.geometry("400x400")

        types = readCSV("./ShopTypes.txt") ## list of NPC types
        
        Types = StringVar()  ## currently selected NPC type
        Types.set(types[0])  

        opt = OptionMenu(self, Types, *types) ## drop down menu select
        opt.pack()

        def NPC_Gen(*args):
            output = StringVar()
            temp = ""
            NPC_Type = ("./" + Types.get() + ".txt") ## file path of inventory csv for selected type
            npcs = readCSV(NPC_Type) ## list of npc possibilities 

            output.set(temp)
            label = Label(self, textvariable = output) ## output label
            label.pack()
            
        button1 = Button(self, text="Generate", command=NPC_Gen) ## button to run process 
        button1.pack()



class DiceRoller(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("Dice Roller") 
        self.geometry("200x200")
        
        result = StringVar() ## output
        dice = StringVar() ## input
        
        def writer(*args):  ## roller call
            result.set(diceRoller(text_entry.get()))
  
        text_entry = Entry(self, textvariable=dice) ## field for dice entry
        text_entry.pack()
        
        button1 = Button(self, text="Roll", command=writer) ## button to roll
        button1.pack()
        
        label = Label(self, textvariable = result) ## results label
        label.pack()
        
        

class ShopInventory(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("Shop Inventory Generator") 
        self.geometry("400x400")
        
        shops = readCSV("./ShopTypes.txt") ## list of shop types
        
        shopTypes = StringVar()  ## currently selected shop
        shopTypes.set(shops[0])  

        opt = OptionMenu(self, shopTypes, *shops) ## drop down menu select
        opt.pack()

        def GenInventory(*args):
            shop = ("./" + shopTypes.get() + "Inventory.txt") ## file path of inventory csv for selected shop
            items = readTupleCSV(shop) ## list of Items
            rarity = {'C':(10,30), 'U':(5,10), 'R':(1,5), 'V':(0,1)} ## rarity to quantity dictionary
            temp = ""
            output = StringVar()

            for i in items:
                temp += (i[0] + ": " + str(randint(rarity[i[1]][0],rarity[i[1]][1])) + " - " + i[2] + "\n")

            output.set(temp)
            label = Label(self, textvariable = output)
            label.pack()
            
        button1 = Button(self, text="Generate", command=GenInventory) 
        button1.pack()

class StatusTracker(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("New Window") 
        self.geometry("200x200")
        
        label = Label(self, text ="This is a new Window")
        label.pack(fill = X, padx=5, pady=5)

class BattlemapGen(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("New Window") 
        self.geometry("400x400")

        terrains = readCSV("./TerrainTypes.txt")
        
        terrainTypes = StringVar()
        terrainTypes.set(terrains[0])
        
        label = Label(self, text ="This is a new Window")
        label.pack(fill = X, padx=5, pady=5)

class MusicManage(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("New Window") 
        self.geometry("200x200")
        
        label = Label(self, text ="This is a new Window")
        label.pack(fill = X, padx=5, pady=5)

class OverlandManage(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("New Window") 
        self.geometry("200x200")
        
        label = Label(self, text ="This is a new Window")
        label.pack(fill = X, padx=5, pady=5)

class CharacterManage(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("New Window") 
        self.geometry("200x200")
        
        label = Label(self, text ="This is a new Window")
        label.pack(fill = X, padx=5, pady=5)

class EncounterGen(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("Encounter Generator") 
        self.geometry("400x400")

        terrains = readCSV("./TerrainTypes.txt")
        
        terrainTypes = StringVar()
        terrainTypes.set(terrains[0])
        
        label = Label(self, text ="This is a new Window")
        label.pack(fill = X, padx=5, pady=5)



##----------------------------------------------------------------------------------------------------------------------------------
##   Launch Hub
##----------------------------------------------------------------------------------------------------------------------------------

        
# creates a Tk() object 
master = Tk()

# set lable font
lblFont = tkFont.Font(family='Helvetica', size=24, weight=tkFont.BOLD)
btnFont = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)

# sets bacckground color
master.configure(background=BgColor)

# sets the geometry of main root window 
master.geometry("600x600")

label = Label(master, text ="Welcome to The Keep", background=lblColor, anchor = 'center', font = lblFont)

label.pack(fill = X, padx=5, pady=15)

equation = StringVar() 
  

# a button widget which will open a new window on button click 
btnDiceRoller = Button(master, text ="Dice Roller", font = btnFont)
btnDiceRoller.bind("<Button>", lambda e: DiceRoller(master))
btnDiceRoller.pack(fill = X, padx=5, pady=8)

btnNpcGen = Button(master, text ="NPC Generator", font = btnFont)
btnNpcGen.bind("<Button>", lambda e: NpcGen(master))
btnNpcGen.pack(fill = X, padx=5, pady=8)


btnNpcGen = Button(master, text ="Music Manager", font = btnFont)
btnNpcGen.bind("<Button>", lambda e: MusicManage(master))
btnNpcGen.pack(fill = X, padx=5, pady=8)


btnNpcGen = Button(master, text ="Shop Inventory Generator", font = btnFont)
btnNpcGen.bind("<Button>", lambda e: ShopInventory(master))
btnNpcGen.pack(fill = X, padx=5, pady=8)


btnNpcGen = Button(master, text ="Battlemap Generator", font = btnFont)
btnNpcGen.bind("<Button>", lambda e: BattlemapGen(master))
btnNpcGen.pack(fill = X, padx=5, pady=8)


btnNpcGen = Button(master, text ="Character Management", font = btnFont)
btnNpcGen.bind("<Button>", lambda e: CharacterManage(master))
btnNpcGen.pack(fill = X, padx=5, pady=8)


btnNpcGen = Button(master, text ="Advanced Status Tracker", font = btnFont)
btnNpcGen.bind("<Button>", lambda e: StatusTracker(master))
btnNpcGen.pack(fill = X, padx=5, pady=8)


btnNpcGen = Button(master, text ="Encounter Generator", font = btnFont)
btnNpcGen.bind("<Button>", lambda e: EncounterGen(master))
btnNpcGen.pack(fill = X, padx=5, pady=8)


btnNpcGen = Button(master, text ="Overland Travel Manager", font = btnFont)
btnNpcGen.bind("<Button>", lambda e: OverlandManage(master))
btnNpcGen.pack(fill = X, padx=5, pady=8)

# mainloop, runs infinitely 
mainloop() 
