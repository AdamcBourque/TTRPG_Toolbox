## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere

from KeepFunctions import *
import SpellManager

class CharacterManage(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master)
        
        self.title("Character Manager")
        self.geometry("1000x600")

        frame = Frame(self)
        frame.pack()

        for i in range (0, 30):
            frame.columnconfigure(i, weight=1)

        # sets bacckground color
        self.configure(background=BgColor)
        frame.configure(background=BgColor)
        
        # Variables
        profs = []
        skillMods = []
        skills = ["Athletics", "Acrobatics", "Sleight of Hand", "Stealth", "Arcana", "History",  "Investigation",
                  "Nature", "Religion", "Animal Handling", "Insight", "Medicine", "Perception", "Survival", "Deception",
                  "Intimidation", "Performance", "Persuasion"]
        
        classes = ["Rogue","Warlock","Paladin","Monk","Wizard","Cleric","Druid","Barbarian","Sorcerer","Ranger","Bard",
                   "Fighter","Artificer"]

        stats = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

        attacks = []
        toHits = []
        damages = []
        
        name = StringVar()
        race = StringVar()
        class_ = StringVar()
        class_.set(classes[0])
        strength = IntVar(stats[0])
        dex = IntVar(stats[0])
        con = IntVar(stats[0])
        inteligence = IntVar(stats[0])
        wis = IntVar(stats[0])
        cha = IntVar(stats[0])
        strengthMod = (strength.get() - 10) / 2
        dexMod = (dex.get() - 10) / 2
        conMod = (con.get() - 10) / 2
        inteligenceMod = (inteligence.get() - 10) / 2
        wisMod = (wis.get() - 10) / 2
        chaMod = (cha.get() - 10) / 2
        level = IntVar(stats[0])
        prof = IntVar()
        passivePerception = 0
        AC = IntVar()
        HP = IntVar()
        movement = IntVar()
        

        weapons = []
        spells= []  ## Spell(name, level) from Spell.py in KeepFunctions.py
        inventory = []
        description = ""
        armorTypes = []

        name_label = Label(frame, fg="white smoke", background=BgColor,  text ="Name")
        name_label.grid(row=2, column=0, padx = 2, pady = 2)
        name_entry = Entry(frame, textvariable=name) ## field for entry
        name_entry.grid(row=2, column=1, padx = 2, pady = 2)

        race_label = Label(frame, fg="white smoke", background=BgColor,  text ="Race")
        race_label.grid(row=2, column=2, padx = 2, pady = 2)
        race_entry = Entry(frame, textvariable=race) ## field for entry
        race_entry.grid(row=2, column=3, padx = 2, pady = 2)

        class_label = Label(frame, fg="white smoke", background=BgColor,  text ="Class")
        class_label.grid(row=2, column=4, padx = 2, pady = 2)
        class_entry = OptionMenu(frame, class_, *classes) ## drop down menu select
        class_entry.config(bg=lblColor)
        class_entry.grid(row=2, column=5, padx = 2, pady = 2)

        level_label = Label(frame, fg="white smoke", background=BgColor,  text ="Level")
        level_label.grid(row=2, column=6, padx = 2, pady = 2)
        level_entry = OptionMenu(frame, level, *stats) ## field for entry
        level_entry.config(bg=lblColor)
        level_entry.grid(row=2, column=7, padx = 2, pady = 2)

        gap_label = Label(frame, fg="white smoke", background=BgColor,  text =" ")
        gap_label.grid(row=3, column=0, padx = 2, pady = 2)
        gap2_label = Label(frame, fg="white smoke", background=BgColor,  text =" ")
        gap2_label.grid(row=4, column=0, padx = 2, pady = 2)

        AC_label = Label(frame, fg="white smoke", background=BgColor,  text ="Armor Class")
        AC_label.grid(row=5, column=4, padx = 2, pady = 2)
        AC_entry = Entry(frame, textvariable=AC) ## field for entry
        AC_entry.grid(row=5, column=5, padx = 2, pady = 2)

        HP_label = Label(frame, fg="white smoke", background=BgColor,  text ="Hit Points")
        HP_label.grid(row=5, column=2, padx = 2, pady = 2)
        HP_entry = Entry(frame, textvariable=HP) ## field for entry
        HP_entry.grid(row=5, column=3, padx = 2, pady = 2)

        strength_label = Label(frame, fg="white smoke", background=BgColor,  text ="Str")
        strength_label.grid(row=5, column=0, padx = 2, pady = 2)
        strength_entry = OptionMenu(frame, strength, *stats) ## field for entry
        strength_entry.config(bg=lblColor)
        strength_entry.grid(row=5, column=1, padx = 2, pady = 2)

        dex_label = Label(frame, fg="white smoke", background=BgColor,  text ="Dex")
        dex_label.grid(row=6, column=0, padx = 2, pady = 2)
        dex_entry = OptionMenu(frame, dex, *stats) ## field for entry
        dex_entry.config(bg=lblColor)
        dex_entry.grid(row=6, column=1, padx = 2, pady = 2)

        con_label = Label(frame, fg="white smoke", background=BgColor,  text ="Con")
        con_label.grid(row=7, column=0, padx = 2, pady = 2)
        con_entry = OptionMenu(frame, con, *stats) ## field for entry
        con_entry.config(bg=lblColor)
        con_entry.grid(row=7, column=1, padx = 2, pady = 2)

        int_label = Label(frame, fg="white smoke", background=BgColor,  text ="Int")
        int_label.grid(row=8, column=0, padx = 2, pady = 2)
        int_entry = OptionMenu(frame, inteligence, *stats) ## field for entry
        int_entry.config(bg=lblColor)
        int_entry.grid(row=8, column=1, padx = 2, pady = 2)

        wis_label = Label(frame, fg="white smoke", background=BgColor,  text ="Wis")
        wis_label.grid(row=9, column=0, padx = 2, pady = 2)
        wis_entry = OptionMenu(frame, wis, *stats) ## field for entry
        wis_entry.config(bg=lblColor)
        wis_entry.grid(row=9, column=1, padx = 2, pady = 2)

        cha_label = Label(frame, fg="white smoke", background=BgColor,  text ="Cha")
        cha_label.grid(row=10, column=0, padx = 2, pady = 2)
        cha_entry = OptionMenu(frame, cha, *stats) ## field for entry
        cha_entry.config(bg=lblColor)
        cha_entry.grid(row=10, column=1, padx = 2, pady = 2)

        attack_label = Label(frame, fg="white smoke", background=BgColor,  text = "Attack")
        attack_label.grid(row=6, column=3, padx = 2, pady = 2)

        hit_label = Label(frame, fg="white smoke", background=BgColor,  text = "To Hit")
        hit_label.grid(row=6, column=4, padx = 2, pady = 2)

        dmg_label = Label(frame, fg="white smoke", background=BgColor,  text = "Damage")
        dmg_label.grid(row=6, column=5, padx = 2, pady = 2)

        

        for i in range (0,5):
            attack = StringVar()
            toHit = StringVar()
            dmg = StringVar()
            attacks.append(attack)
            toHits.append(toHit)
            damages.append(dmg)
            atk_entry = Entry(frame, textvariable = attacks[i])
            atk_entry.grid(row=(7+i), column=3, padx = 2, pady = 2)
            hit_entry = Entry(frame, textvariable = toHits[i])
            hit_entry.grid(row=(7+i), column=4, padx = 2, pady = 2)
            dmg_entry = Entry(frame, textvariable = damages[i])
            dmg_entry.grid(row=(7+i), column=5, padx = 2, pady = 2)


        gap3_label = Label(frame, fg="white smoke", background=BgColor,  text =" ")
        gap3_label.grid(row=13, column=0, padx = 2, pady = 2)

        lvl = level.get()

        if (lvl >= 17):
            prof = 6
        elif (lvl >= 13):
            prof = 5
        elif (lvl >= 9):
            prof = 4
        elif (lvl >= 5):
            prof = 3
        else:
            prof = 2

        for i in range (0,18):
            sProf = IntVar()
            sMod = IntVar()
            skill = skills[i]
            Checkbutton(frame, fg="white smoke", bg=BgColor, text=skill, variable=sProf).grid(row=(14+int(i/3)), column=2*(i%3))
            Entry(frame, textvariable = sMod, width = 3).grid(row=(14+int(i/3)), column=2*(i%3)+1)
            profs.append(sProf)
            skillMods.append(sMod)

        def loadFromCsv():
            filename = filedialog.askopenfilename(initialdir = "./Sheets", title = "Select a File", filetypes = (("Text", "*.txt*"), ("all files",  "*.*")))
            data = readCSV(filename)  ## reads in the data frome the csv selected above
            if (data[0] != ""):
                name.set(data[0])
            if (data[1] != ""):
                race.set(data[1])
            if (data[2] != ""):
                class_.set(data[2])
            if (data[3] != ""):
                level.set(int(data[3]))
            if (data[4] != ""):
                strength.set(int(data[4]))
            if (data[5] != ""):
                dex.set(int(data[5]))
            if (data[6] != ""):
                con.set(int(data[6]))
            if (data[7] != ""):
                inteligence.set(int(data[7]))
            if (data[8] != ""):
                wis.set(int(data[8]))
            if (data[9] != ""):
                cha.set(int(data[9]))
            if (data[10] != ""):
                prof = int(data[10])
            if (data[11] != ""):
                HP.set(int(data[11]))
            if (data[12] != ""):
                AC.set(int(data[12]))
            temp = 13
            for i in profs:
                if (data[temp] != ""):
                    i.set(data[temp])
                temp = temp + 1
            for j in skillMods:
                 if (data[temp] != ""):
                    j.set(int(data[temp]))
                 temp = temp + 1
            for k in range (0,5):
                 if (data[temp] != ""):
                    attacks[k].set(data[temp])
                 if (data[temp + 1] != ""):
                    toHits[k].set(data[temp +1])
                 if (data[temp + 2] != ""):
                    damages[k].set(data[temp +2])
                 temp = temp + 3
                

        def saveToCsv():
            output = ""  ## holds the fields in the form of a csv
            output += name.get() + ","
            output += race.get() + ","
            output += class_.get() + ","
            output += str(level.get()) + ","
            output += str(strength.get()) + ","
            output += str(dex.get()) + ","
            output += str(con.get()) + ","
            output += str(inteligence.get()) + ","
            output += str(wis.get()) + ","
            output += str(cha.get()) + ","
            output += str(prof) + ","
            output += str(HP.get()) + ","
            output += str(AC.get()) + ","
            for i in profs:
                output += str(i.get()) + ","
            for j in skillMods:
                output += str(j.get()) + ","
            for k in range (0,5):
                output += attacks[k].get() + "," + toHits[k].get() + "," + damages[k].get()+ ","
                
            sheet = open("./Sheets/" + name.get() + ".txt", "w") ## writes output to file "name.txt"
            sheet.write(output)
            sheet.close()

            
        btnSave = Button(frame, bg=lblColor, fg="white smoke", text ="Save")
        btnSave.bind("<Button>", lambda e: saveToCsv())
        btnSave.grid(row=2, column=9, padx = 2, pady = 2)

        btnLoad = Button(frame, bg=lblColor, fg="white smoke", text ="Load")
        btnLoad.bind("<Button>", lambda e: loadFromCsv())
        btnLoad.grid(row=2, column=10, padx = 2, pady = 2)

        new_frame = Frame(self)
        new_frame.pack()

##        name_label = Label(new_frame, fg="white smoke", text ="Loadout")
##        name_label.grid(row=1, column=0, padx = 2, pady = 2)
##        name_entry = OptionMenu(new_frame, fg="white smoke", )
##        name_entry.grid(row=1, column=1, padx = 2, pady = 2)
