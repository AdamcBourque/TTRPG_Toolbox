## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere

from KeepFunctions import *
import SpellManager

action = True
bonus_action = True
reaction = True
concentration = False

class StatusTracker(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("Status Tracker") 
        self.geometry("825x600")
        self.iconbitmap(r"The-Keep.ico")

        # set label font
        lblFont = tkFont.Font(family='Helvetica', size=24, weight=tkFont.BOLD)
        btnFont = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)

        # sets background color
        self.configure(background=BgColor)

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
        
        movement = 0
        cond_list = ''
        
        frame = Frame(self)
        frame.config(bg = BgColor)
        frame.pack()

        char_name = StringVar()
        char_name.set("Your Character")

        char_name_label = Label(frame, fg="white smoke", background=BgColor, text ="Character Name")
        char_name_label.grid(row=1, column=0, padx = 2, pady = 2)
        char_name_entry = OptionMenu(frame, char_name, *chars) ## drop down menu select
        char_name_entry.config(fg="white smoke", background=lblColor, highlightbackground = BgColor, highlightcolor = BgColor)
        char_name_entry.grid(row=1, column=1, padx = 2, pady = 2)

        condition_name = StringVar()
        condition_name.set(conditions[0])

        condition_name_label = Label(frame, fg="white smoke", background=BgColor, text ="Condition")
        condition_name_label.grid(row=1, column=2, padx = 2, pady = 2)
        condition_name_entry = OptionMenu(frame, condition_name, *conditions) ## drop down menu select
        condition_name_entry.config(fg="white smoke", background=lblColor, highlightbackground = BgColor, highlightcolor = BgColor)
        condition_name_entry.grid(row=1, column=3, padx = 2, pady = 2)

        btnAfflict = Button(frame, fg="white smoke", background=lblColor, text ="Add Condition")
        btnAfflict.bind("<Button>", lambda e: add_condition())
        btnAfflict.grid(row=1, column=4, padx = 2, pady = 2)

        btnCure = Button(frame, fg="white smoke", background=lblColor, text ="Cure Condition")
        btnCure.bind("<Button>", lambda e: clear_condition(condition_name.get()))
        btnCure.grid(row=1, column=5, padx = 2, pady = 2)

        btnReset = Button(frame, fg="white smoke", background=lblColor, text ="Reset")
        btnReset.bind("<Button>", lambda e: reset())
        btnReset.grid(row=1, column=6, padx = 2, pady = 2)

        btnLong = Button(frame, fg="white smoke", background=lblColor, text ="Long Rest")
        btnLong.bind("<Button>", lambda e: long_rest())
        btnLong.grid(row=2, column=0, padx = 2, pady = 2)

        btnShort = Button(frame, fg="white smoke", background=lblColor, text ="Short Rest")
        btnShort.bind("<Button>", lambda e: short_rest())
        btnShort.grid(row=2, column=1, padx = 2, pady = 2)

        btnNewRound = Button(frame, fg="white smoke", background=lblColor, text ="New Round")
        btnNewRound.bind("<Button>", lambda e: new_turn())
        btnNewRound.grid(row=2, column=2, padx = 2, pady = 2)

        btnAction = Button(frame, fg="white smoke", background=lblColor, text ="Action")
        btnAction.bind("<Button>", lambda e: action())
        btnAction.grid(row=2, column=3, padx = 2, pady = 2)

        btnBonusAction = Button(frame, fg="white smoke", background=lblColor, text ="Bonus Action")
        btnBonusAction.bind("<Button>", lambda e: bonus_action())
        btnBonusAction.grid(row=2, column=4, padx = 2, pady = 2)

        btnReaction = Button(frame, fg="white smoke", background=lblColor, text ="Reaction")
        btnReaction.bind("<Button>", lambda e: reaction())
        btnReaction.grid(row=2, column=5, padx = 2, pady = 2)

        btnCon = Button(frame, fg="white smoke", background=lblColor, text ="Concentrating")
        btnCon.bind("<Button>", lambda e: concentrate())
        btnCon.grid(row=2, column=6, padx = 2, pady = 2)


        def long_rest():
            global action, bonus_action, reaction
            action = True
            bonus_action = True
            reaction = True
            economy()

        def short_rest():
            global action, bonus_action, reaction
            action = True
            bonus_action = True
            reaction = True
            economy()

        def new_turn():
            global action, bonus_action, reaction
            action = True
            bonus_action = True
            reaction = True
            economy()

        def action():
            global action
            action = False
            economy()
            
            
        def bonus_action():
            global bonus_action
            bonus_action = False
            economy()
            
        def reaction():
            global reaction
            reaction = False
            economy()

        def concentrate():
            global concentration
            concentration = not concentration
            economy()

        def reset():
            global action, bonus_action, reaction, concentration
            char_name.set("Your Character")
            condition_name.set(conditions[0])
            while(len(char_conditions) != 0):
                char_conditions.remove(char_conditions[0])
            action = True
            bonus_action = True
            reaction = True
            concentration = False
            movement = 0
            economy()
            conditions_label.config(text = '')
            conditions_label.pack()

        def add_condition():
            has = False
            if (char_conditions != []):
                for i in char_conditions:
                    if (i == condition_name.get()):
                        has = True
            if (has == False):
                char_conditions.append(condition_name.get())
            cond_list = display_conditions()
            conditions_label.config(text = cond_list)
            conditions_label.pack()

        def clear_condition(condition):
            if (char_conditions.count(condition) != 0):
                char_conditions.remove(condition)
            cond_list = display_conditions()
            conditions_label.config(text = cond_list)
            conditions_label.pack()

        def display_conditions():
            output = ''
            temp = 0
            for i in char_conditions:
                temp = conditions.index(i)
                descript = condition_descriptions[temp].replace('*', "\n\u2022 ")
                output += i + '\n' + descript + '\n' + "---------------------------------------------------------------------------" + '\n'
            return output


        def economy():
            global action, bonus_action, reaction
            if (action == False):
                btnAction.config(bg = "#8a2121")
                btnAction.grid(row=2, column=3, padx = 2, pady = 2)
            else:
                btnAction.config(bg = lblColor)
                btnAction.grid(row=2, column=3, padx = 2, pady = 2)
            if (bonus_action == False):
                btnBonusAction.config(bg = "#8a2121")
                btnBonusAction.grid(row=2, column=4, padx = 2, pady = 2)
            else:
                btnBonusAction.config(bg = lblColor)
                btnBonusAction.grid(row=2, column=4, padx = 2, pady = 2)
            if (reaction == False):
                btnReaction.config(bg = "#8a2121")
                btnReaction.grid(row=2, column=5, padx = 2, pady = 2)
            else:
                btnReaction.config(bg = lblColor)
                btnReaction.grid(row=2, column=5, padx = 2, pady = 2)
            if (concentration == True):
                btnCon.config(bg = "#8a2121")
                btnCon.grid(row=2, column=6, padx = 2, pady = 2)
            else:
                btnCon.config(bg = lblColor)
                btnCon.grid(row=2, column=6, padx = 2, pady = 2)


        new_frame = Frame(self)
        new_frame.config(background=BgColor)
        new_frame.pack()

        conditions_label = Label(new_frame, fg="white smoke", background=BgColor, text = cond_list)

        div = '\n' + "============================================== CONDITIONS ==============================================" + '\n'
        div_label = Label(new_frame, fg="white smoke", background=BgColor, text = div)
        div_label.pack()

        

  
