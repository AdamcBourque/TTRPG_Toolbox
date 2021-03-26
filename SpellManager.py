## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere

from KeepFunctions import *
from Spell import *

class SpellManager(Toplevel):

    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("Spell Manager") 
        self.geometry("800x600")

        spells = readTupleCSV2("./CSVs/Spells.txt")
        cantrips = []
        first = []
        second = []
        third = []
        fourth = []
        fifth = []
        sixth = []
        seventh = []
        eighth = []
        ninth = []
        levels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        slots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        level = IntVar()
        level.set(levels[0])
        
        for i in range (0, len(spells)):
            temp = spells[i].replace("(",'')
            temp = temp.replace(")",'')
            temp = temp.split(',')
            spells[i] = temp[0]

        level_label = Label(self, text ="Spell Level")
        level_label.grid(row=1, column=0, padx = 2, pady = 2)
        level_entry = OptionMenu(self, level, *levels) ## field for entry
        level_entry.grid(row=1, column=1, padx = 2, pady = 2)
