## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere

from KeepFunctions import *

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
        
        
