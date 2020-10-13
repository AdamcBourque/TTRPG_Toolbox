# This will import all the widgets 
# and modules which are available in 
# tkinter and ttk module 
from tkinter import *
from tkinter import font as tkFont

expression = ""
BgColor = "grey19"
lblColor = "grey35"
##fontColor = "pink"

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
        self.title("Newer Window") 
        self.geometry("200x200")
        global expression
        expression_field = Entry(self, textvariable=equation) 
        expression_field.pack(fill = X, padx=5, pady=5)
        equation.set('enter your expression') 
        equation.set(expression)
        label = Label(self, text = equation)
        label.pack(fill = X, padx=5, pady=5)

class ShopInventory(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("New Window") 
        self.geometry("200x200") 
        label = Label(self, text ="This is a new Window")
        label.pack(fill = X, padx=5, pady=5)

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
