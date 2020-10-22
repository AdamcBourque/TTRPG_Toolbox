from tkinter import *
from tkinter import font as tkFont
from re import split      ## for re.split
from random import *  ## for pseudorandom number generation


BgColor = "grey19"
lblColor = "grey35"
##fontColor = "pink"

## dice roller function takes a string "2d8+5" and prints the rolls and total.
## returns total as an int
def diceRoller(diceString):
    ## print("Rolling " + diceString + "\n")
    elems = re.split('[+-]', diceString) ##splits into dice types and mod

    if (elems[-1].find('d') == -1): ## Checks if there is a modifier
        mod = elems[-1] ## stat modifier
        totalRoll = ""
        total = int(mod)
        for j in range (0, len(elems)-1):
            dice = elems[j].split('d') ## seperates dice quantity and sizes
            for i in range (0, int(dice[0])):
                temp = randint(1, int(dice[1])) 
                total += temp ## adds each dice roll to the total
                totalRoll += (str(temp) + " + ") ## adds each roll to the return string
        totalRoll += (str(mod) + " = " + str(total))
    else:
        mod = 0
        totalRoll = ""
        total = int(mod)
        for j in range (0, len(elems)):
            dice = elems[j].split('d') ## seperates dice quantity and sizes
            for i in range (0, int(dice[0])):
                temp = randint(1, int(dice[1])) 
                total += temp ## adds each dice roll to the total
                totalRoll += (str(temp) + " + ") ## adds each roll to the return string
        totalRoll += (" = " + str(total))
    return totalRoll

## returns one item from a coma seperatied list read from a file
def selectFromFile(file):  
    text = file.read() 
    items = text.split(",")
    items[0] = items[0].replace("ï»¿", '') ## remove garbage from front of string
    return items[randint(0,len(items)-1)]

## These classes will be the other tool GUI's
class NpcGen(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("New Window") 
        self.geometry("200x200")
        
        label = Label(self, text ="This is a new Window")
        label.pack(fill = X, padx=5, pady=5)


class DiceRoller(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("Dice Roller") 
        self.geometry("200x200")
        
        result = StringVar() ## output
        dice = StringVar() ## input
        
        def writer(*args):  ## roller call
            result.set(diceRoller(text_entry.get()))
  
        text_entry = Entry(self, textvariable=dice)
        text_entry.pack()
        
        button1 = Button(self, text="Roll", command=writer) 
        button1.pack()
        
        label = Label(self, textvariable = result)
        label.pack()
        
        

class ShopInventory(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("Shop Inventory Generator") 
        self.geometry("200x200")
        
        file = open("./TerrainTypes.txt", "r") ## shop types file
        shops = file.read().split(',') ## shop type list
        shops[0] = shops[0].replace("ï»¿", '') ## remove garbage from front of string
        file.close()
        
        shopTypes = StringVar()
        shopTypes.set(shops[0])

        opt = OptionMenu(self, shopTypes, *shops) ## drop down menu select
        opt.pack()
        
        label = Label(self, text ="This is a new Window")
        label.pack()

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
        self.geometry("200x200")
        
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
        self.title("New Window") 
        self.geometry("200x200")
        
        label = Label(self, text ="This is a new Window")
        label.pack(fill = X, padx=5, pady=5)

        
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
