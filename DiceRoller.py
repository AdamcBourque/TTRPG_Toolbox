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

        # set lable font
        lblFont = tkFont.Font(family='Helvetica', size=24, weight=tkFont.BOLD)
        btnFont = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)

        # sets bacckground color
        self.configure(background=BgColor)
        
        result = StringVar() ## output
        dice = StringVar() ## input
        
        def writer(*args):  ## roller call
            result.set(diceRoller(text_entry.get()))
  
        text_entry = Entry(self, textvariable=dice) ## field for dice entry
        text_entry.pack()
        
        button1 = Button(self, fg="white smoke", background=lblColor, text="Roll", command=writer) ## button to roll
        button1.pack()
        
        label = Label(self, fg="white smoke", background=BgColor, textvariable = result) ## results label
        label.pack()
        
        
