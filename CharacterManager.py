from tkinter import *
from tkinter import font as tkFont
from re import split      ## for re.split
from random import *  ## for pseudorandom number generation
from tkinter import filedialog


from KeepFunctions import *


class CharacterManage(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master)
        
        self.title("Character Manager")
        self.geometry("600x600")

        # Variables
        name = StringVar()
        class_ = StringVar()
        strength = StringVar()
        dex = StringVar()
        con = StringVar()
        inteligence = StringVar()
        wis = StringVar()
        cha = StringVar()
        level = StringVar()
        prof = StringVar()
        Athletics = StringVar()
        Acrobatics = StringVar()
        Sleight_of_Hand = StringVar()
        Stealth = StringVar()
        Arcana = StringVar()
        History = StringVar()
        Investigation = StringVar()
        Nature = StringVar()
        Religion = StringVar()
        Animal_Handling = StringVar()
        Insight = StringVar()
        Medicine = StringVar()
        Perception = StringVar()
        Survival = StringVar()
        Deception = StringVar()
        Intimidation = StringVar()
        Performance = StringVar()
        Persuasion = StringVar()
        classes = {"Rogue","Warlock"} ## add more

        name_label = Label(self, text ="Name")
        name_label.grid(row=2, column=0, padx = 2, pady = 2)
        name_entry = Entry(self, textvariable=name) ## field for entry
        name_entry.grid(row=2, column=1, padx = 2, pady = 2)

        class_label = Label(self, text ="class")
        class_label.grid(row=2, column=3, padx = 2, pady = 2)
        class_entry = Entry(self, textvariable=class_) ## field for entry
        class_entry.grid(row=2, column=4, padx = 2, pady = 2)

        level_label = Label(self, text ="Level")
        level_label.grid(row=2, column=6, padx = 2, pady = 2)
        level_entry = Entry(self, textvariable=level) ## field for entry
        level_entry.grid(row=2, column=7, padx = 2, pady = 2)

        strength_label = Label(self, text ="Str")
        strength_label.grid(row=5, column=0, padx = 2, pady = 2)
        strength_entry = Entry(self, textvariable=strength) ## field for entry
        strength_entry.grid(row=5, column=1, padx = 2, pady = 2)

        dex_label = Label(self, text ="Dex")
        dex_label.grid(row=7, column=0, padx = 2, pady = 2)
        dex_entry = Entry(self, textvariable=dex) ## field for entry
        dex_entry.grid(row=7, column=1, padx = 2, pady = 2)

        con_label = Label(self, text ="Con")
        con_label.grid(row=9, column=0, padx = 2, pady = 2)
        con_entry = Entry(self, textvariable=con) ## field for entry
        con_entry.grid(row=9, column=1, padx = 2, pady = 2)

        int_label = Label(self, text ="Int")
        int_label.grid(row=11, column=0, padx = 2, pady = 2)
        int_entry = Entry(self, textvariable=inteligence) ## field for entry
        int_entry.grid(row=11, column=1, padx = 2, pady = 2)

        wis_label = Label(self, text ="Wis")
        wis_label.grid(row=13, column=0, padx = 2, pady = 2)
        wis_entry = Entry(self, textvariable=wis) ## field for entry
        wis_entry.grid(row=13, column=1, padx = 2, pady = 2)

        cha_label = Label(self, text ="Cha")
        cha_label.grid(row=15, column=0, padx = 2, pady = 2)
        cha_entry = Entry(self, textvariable=cha) ## field for entry
        cha_entry.grid(row=15, column=1, padx = 2, pady = 2)

        lvl = int(level.get())

        if (lvl >= 17):
            prof = "6"
        elif (lvl >= 13):
            prof = "5"
        elif (lvl >= 9):
            prof = "4"
        elif (lvl >= 5):
            prof = "3"
        else:
            prof = "2"



