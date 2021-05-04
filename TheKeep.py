## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere

from NpcGen import *
from DiceRoller import *
from InventoryGen import *
from CharacterManager import *
from BattlemapGen import *
from MusicManager import *
from EncounterGen import *
from NpcGen import *
from OverlandManage import *
from StatusTracker import *
from SpellManager import *


##----------------------------------------------------------------------------------------------------------------------------------
##   Launch Hub
##----------------------------------------------------------------------------------------------------------------------------------

        
# creates a Tk() object 
master = Tk()
master.title("The Keep")

# set lable font
lblFont = tkFont.Font(family='Helvetica', size=24, weight=tkFont.BOLD)
btnFont = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)

# sets bacckground color
master.configure(background=BgColor)

# sets the geometry of main root window 
master.geometry("600x700")

label = Label(master, text ="Welcome to The Keep", background=BgColor, fg = 'white smoke', anchor = 'center', font = lblFont)

label.pack(fill = X, padx=5, pady=15)

equation = StringVar() 
  

# a button widget which will open a new window on button click 
btnDiceRoller = Button(master, background=lblColor, fg='white smoke', text ="Dice Roller", font = btnFont)
btnDiceRoller.bind("<Button>", lambda e: DiceRoller(master))
btnDiceRoller.pack(fill = X, padx=5, pady=8)

btnNpcGen = Button(master, background=lblColor, fg='white smoke', text ="NPC Generator", font = btnFont)
btnNpcGen.bind("<Button>", lambda e: NpcGen(master))
btnNpcGen.pack(fill = X, padx=5, pady=8)


btnMusic = Button(master, background=lblColor, fg='white smoke', text ="Music Manager", font = btnFont)
btnMusic.bind("<Button>", lambda e: MusicManage(master))
btnMusic.pack(fill = X, padx=5, pady=8)


btnShop = Button(master, background=lblColor, fg='white smoke', text ="Shop Inventory Generator", font = btnFont)
btnShop.bind("<Button>", lambda e: ShopInventory(master))
btnShop.pack(fill = X, padx=5, pady=8)


btnBattlemap = Button(master, background=lblColor, fg='white smoke', text ="Battlemap Generator", font = btnFont)
btnBattlemap.bind("<Button>", lambda e: BattlemapGen(master))
btnBattlemap.pack(fill = X, padx=5, pady=8)


btnChar = Button(master, background=lblColor, fg='white smoke', text ="Character Management", font = btnFont)
btnChar.bind("<Button>", lambda e: CharacterManage(master))
btnChar.pack(fill = X, padx=5, pady=8)


btnStatus = Button(master, background=lblColor, fg='white smoke', text ="Advanced Status Tracker", font = btnFont)
btnStatus.bind("<Button>", lambda e: StatusTracker(master))
btnStatus.pack(fill = X, padx=5, pady=8)


btnEncounter = Button(master, background=lblColor, fg='white smoke', text ="Encounter Generator", font = btnFont)
btnEncounter.bind("<Button>", lambda e: EncounterGen("Keep", 0, 0))
btnEncounter.pack(fill = X, padx=5, pady=8)


btnOverland = Button(master, background=lblColor, fg='white smoke', text ="Overland Travel Manager", font = btnFont)
btnOverland.bind("<Button>", lambda e: OverlandManage(master))
btnOverland.pack(fill = X, padx=5, pady=8)

btnSpell = Button(master, background=lblColor, fg='white smoke', text ="Spell Manager", font = btnFont)
btnSpell.bind("<Button>", lambda e: SpellManager(master))
btnSpell.pack(fill = X, padx=5, pady=8)

# mainloop, runs infinitely 
mainloop() 
