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

        frame = Frame(self)
        frame.config(bg = BgColor)
        frame.pack()

        lblfrme = Frame(self)
        lblfrme.config(bg = BgColor)
        lblfrme.pack()
  
        text_entry = Entry(frame, textvariable=dice) ## field for dice entry
        text_entry.grid(row=1, column=0, padx = 2, pady = 2)
        
        button1 = Button(frame, fg="white smoke", background=lblColor, text="Roll", command=writer) ## button to roll
        button1.grid(row=1, column=1, padx = 2, pady = 2)

        filler = Label(lblfrme, fg="white smoke", background=BgColor, textvariable = '') ## results label
        filler.grid(row=2, column=0, padx = 2, pady = 2)
        
        label = Label(lblfrme, fg="white smoke", background=BgColor, textvariable = result) ## results label
        label.grid(row=3, column=0, padx = 2, pady = 2)
        
        
