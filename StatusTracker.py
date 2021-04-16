## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere

from KeepFunctions import *

class StatusTracker(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("Status Tracker") 
        self.geometry("800x600")

        terrains = readCSV("./CSVs/TerrainTypes.txt")
        features = readCSV("./CSVs/TerrainTypes.txt") ## temp
        sizes = ["Small","Medium","Large"]
        chars = listdir("./Sheets")
        conditions = readTupleCSV2("./CSVs/Conditions.txt")
        condition_descriptions = []
        for i in range (0, len(conditions)):
            temp = conditions[i].replace("(",'')
            temp = temp.replace(")",'')
            temp = temp.split(',')
            condition_descriptions.append(temp[1])
            conditions[i] = temp[0]
                
        spell_slots = []
        other_resource = []
        char_conditions = []
        hit_dice = 0
        action = True
        bonus_action = True
        reaction = True
        movement = 0
        
        frame = Frame(self)
        frame.pack()

        char_name = StringVar()
        char_name.set("Your Character")

        char_name_label = Label(frame, text ="Map Name")
        char_name_label.grid(row=1, column=0, padx = 2, pady = 2)
        char_name_entry = OptionMenu(frame, char_name, *chars) ## drop down menu select
        char_name_entry.grid(row=1, column=2, padx = 2, pady = 2)

        condition_name = StringVar()
        condition_name.set(conditions[0])

        condition_name_label = Label(frame, text ="Condition")
        condition_name_label.grid(row=1, column=3, padx = 2, pady = 2)
        condition_name_entry = OptionMenu(frame, condition_name, *conditions) ## drop down menu select
        condition_name_entry.grid(row=1, column=4, padx = 2, pady = 2)

        btnAfflict = Button(frame, text ="Add Condition")
        btnAfflict.bind("<Button>", lambda e: add_condition())
        btnAfflict.grid(row=1, column=5, padx = 2, pady = 2)

        btnLong = Button(frame, text ="Long Rest")
        btnLong.bind("<Button>", lambda e: long_rest())
        btnLong.grid(row=2, column=0, padx = 2, pady = 2)

        btnShort = Button(frame, text ="Short Rest")
        btnShort.bind("<Button>", lambda e: short_rest())
        btnShort.grid(row=2, column=1, padx = 2, pady = 2)

        btnNewRound = Button(frame, text ="New Round")
        btnNewRound.bind("<Button>", lambda e: new_turn())
        btnNewRound.grid(row=2, column=2, padx = 2, pady = 2)

        

        def import_char():
            temp = "not implemented"

        def long_rest():
            char_conditions = []
            action = True
            bonus_action = True
            reaction = True

        def short_rest():
            action = True
            bonus_action = True
            reaction = True

        def new_turn():
            action = True
            bonus_action = True
            reaction = True

        def reset():
            char_name.set("Your Character")
            condition_name.set(conditions[0])
            spell_slots = []
            other_resource = []
            char_conditions = []
            action = True
            bonus_action = True
            reaction = True
            movement = 0

        def add_condition():
            has = False
            if (char_conditions != []):
                for i in char_conditions:
                    if (i == condition_name.get()):
                        has = True
            if (has == False):
                char_conditions.append(condition_name.get())

        def add_spell():
            temp = "not implemented"

        new_frame = Frame(self)
        new_frame.pack()

        

  
