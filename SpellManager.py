## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere

from KeepFunctions import *
from Spell import *

sorted_spells = ["Select Spell"]

class SpellManager(Toplevel):

    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("Spell Manager") 
        self.geometry("950x600")
        self.iconbitmap(r"The-Keep.ico")

        # set lable font
        lblFont = tkFont.Font(family='Helvetica', size=24, weight=tkFont.BOLD)
        btnFont = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)

        # sets bacckground color
        self.configure(background=BgColor)


        spells = readTupleCSV2("./CSVs/Spells.txt")
        spells_ = []
        spell_list = []
        
        levels = ["All Levels", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        slots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        num_slots = [0,1,2,3,4]
        schools = ["All Schools", "Conjuration", "Illusion", "Evocation", "Divination", "Abjuration", "Enchantment", "Transmutation", "Necromancy"]

        level = IntVar()
        level.set(levels[0])

        name = StringVar()

        slot_holder = StringVar()
         
        for i in range (0, len(spells)):
            temp = spells[i]
            temp = temp.replace('(','')
            temp = temp.replace(')','')
            temp = temp.split(',')
            
            spells_.append(Spell(temp))


        frame = Frame(self)
        frame.config(background = BgColor)
        frame.pack()

        output_frame = Frame(self)
        output_frame.config(background = BgColor)
        output_frame.pack()
        
##        name_label = Label(frame, fg = "white smoke", background = BgColor, text ="Character Name")
##        name_label.grid(row=1, column=0, padx = 2, pady = 2)
##        name_entry = Entry(frame, textvariable=name) ## field for entry
##        name_entry.grid(row=1, column=1, padx = 2, pady = 2)
##
##        level_label = Label(frame, fg = "white smoke", background = BgColor, text ="Slot Level")
##        level_label.grid(row=1, column=2, padx = 2, pady = 2)
##        level_entry = OptionMenu(frame, level, *levels) ## field for entry
##        level_entry.config(bg=lblColor, fg = 'white smoke')
##        level_entry.grid(row=1, column=3, padx = 2, pady = 2)
##
##        slot_number_entry = OptionMenu(frame, slot_holder, *num_slots)
##        slot_number_entry.config(bg=lblColor, fg = 'white smoke')
##        slot_number_entry.grid(row=1, column=5, padx = 2, pady = 2)


        # Sets number of spell slots at set level
        def Add_slots():
            slots[level.get()] = int(slot_holder.get())

##        btnSlots = Button(frame, bg=lblColor, fg="white smoke", text ="Add Slots")
##        btnSlots.bind("<Button>", lambda e: Add_slots())
##        btnSlots.grid(row=1, column=4, padx = 2, pady = 2)

        spell_level = StringVar()
        spell_level.set("All")
        school = StringVar()
        school.set("All Schools")
        spell_name = StringVar()
        spell_name.set("All Spells")
        cast_time = StringVar()
        cast_time.set("All")
        

        spell_name_label = Label(frame, fg = "white smoke", background = BgColor, text ="Spell Name")
        spell_name_label.grid(row=2, column=0, padx = 2, pady = 2)
        spell_name_entry = Entry(frame, textvariable = spell_name) ## field for entry
        spell_name_entry.grid(row=2, column=1, padx = 2, pady = 2)

        spell_level_label = Label(frame, fg = "white smoke", background = BgColor, text ="Level")
        spell_level_label.grid(row=2, column=2, padx = 2, pady = 2)
        spell_level_entry = OptionMenu(frame, spell_level, *levels) ## field for entry
        spell_level_entry.config(fg="white smoke", background=lblColor, highlightbackground = BgColor, highlightcolor = BgColor)
        spell_level_entry.grid(row=2, column=3, padx = 2, pady = 2)

        School_label = Label(frame, fg = "white smoke", background = BgColor, text ="School")
        School_label.grid(row=2, column=4, padx = 2, pady = 2)
        School_entry = OptionMenu(frame, school, *schools)
        School_entry.config(fg="white smoke", background=lblColor, highlightbackground = BgColor, highlightcolor = BgColor)
        School_entry.grid(row=2, column=5, padx = 2, pady = 2)

        selected_spell = StringVar()
        selected_spell.set(sorted_spells[0])

        spell_list_entry = OptionMenu(frame, selected_spell, *sorted_spells) ## field for entry
        spell_list_entry.config(fg="white smoke", background=lblColor, highlightbackground = BgColor, highlightcolor = BgColor)
        spell_list_entry.grid(row=3, column=3, padx = 2, pady = 2)

        spell_loadout_label = Label(output_frame, fg = "white smoke", background = BgColor, text = "")
        spell_loadout_label.grid(row=0, column=0, padx = 2, pady = 2)

        def Spell_Search(spell_list_entry):
            global sorted_spells
            sorted_spells = ["Select Spell"]
            if (spell_name.get() == ""):
                spell_name.set("All Spells")
            
            for i in spells_:
                if (((spell_name.get() == "All Spells") or (i.name == spell_name.get())) and
                    ((spell_level.get() == "All Levels") or (i.lvl == spell_level.get())) and
                     ((school.get() == "All Schools") or (i.school == school.get())) and
                      ((cast_time.get() == "All") or (i.action == cast_time.get()))):   

                    sorted_spells.append(i.name)
                     
                    spell_list_entry.destroy()
                    spell_list_entry = OptionMenu(frame, selected_spell, *sorted_spells) ## field for entry
                    spell_list_entry.config(fg="white smoke", background=lblColor, highlightbackground = BgColor, highlightcolor = BgColor)
                    spell_list_entry.grid(row=3, column=3, padx = 2, pady = 2)
                     

        def Add_Spell(selected_spell, spell_loadout_label):
            for i in spells_:
                if (i.name == selected_spell and i not in spell_list):
                    spell_list.append(i)
            output = format_output(name.get(), spell_list)
            spell_loadout_label.config(text = output)
            

        btnSearch = Button(frame, bg=lblColor, fg="white smoke", text ="Search")
        btnSearch.bind("<Button>", lambda e: Spell_Search(spell_list_entry))
        btnSearch.grid(row=3, column=2, padx = 2, pady = 2)
        
        btnAddSpell = Button(frame, bg=lblColor, fg="white smoke", text ="Add Spell")
        btnAddSpell.bind("<Button>", lambda e: Add_Spell(selected_spell.get(), spell_loadout_label))
        btnAddSpell.grid(row=3, column=5, padx = 2, pady = 2)

        def format_output(LoadoutName, spell_list):
            output = "Cantrips: "
            for i in spell_list:
                if (int(i.lvl) == 0):
                    output = output + i.name + ", "
            output = output.strip(", ") + '\n' + "1st Level: "
            for i in spell_list:
                if (int(i.lvl) == 1):
                    output = output + i.name + ", "
            output = output.strip(", ") + '\n' + "2nd Level: "
            for i in spell_list:
                if (int(i.lvl) == 2):
                    output = output+ i.name + ", "
            output = output.strip(", ") + '\n' + "3rd Level: "
            for i in spell_list:
                if (int(i.lvl) == 3):
                    output = output + i.name + ", "
            output = output.strip(", ") + '\n' + "4th Level: "
            for i in spell_list:
                if (int(i.lvl) == 4):
                    output = output + i.name + ", "
            output = output.strip(", ") + '\n' + "5th Level: "
            for i in spell_list:
                if (int(i.lvl) == 5):
                    output = output + i.name + ", "
            output = output.strip(", ") + '\n' + "6th Level: "
            for i in spell_list:
                if (int(i.lvl) == 6):
                    output = output + i.name + ", "
            output = output.strip(", ") + '\n' + "7th Level: "
            for i in spell_list:
                if (int(i.lvl) == 7):
                    output = output + i.name + ", "
            output = output.strip(", ") + '\n' + "8th Level: "
            for i in spell_list:
                if (int(i.lvl) == 8):
                    output = output + i.name + ", "
            output = output.strip(", ") + '\n' + "9th Level: "
            for i in spell_list:
                if (int(i.lvl) == 9):
                    output = output + i.name + ", "
            output.strip(", ")
            return output

        def Save_Loadout(output):
            file = filedialog.asksaveasfile(initialdir = "./Sheets/SpellLoadouts/", title = "Select a File", defaultextension = ".txt")
            temp = ''
            for i in spell_list:
                temp += i.name + ','
            file.write(temp)
            file.close()

        btnSave = Button(frame, bg=lblColor, fg="white smoke", text ="Save Loadout")
        btnSave.bind("<Button>", lambda e: Save_Loadout(format_output(name.get(), spell_list)))
        btnSave.grid(row=3, column=0, padx = 2, pady = 2)

        btnLoad = Button(frame, bg=lblColor, fg="white smoke", text ="Load Loadout")
        btnLoad.bind("<Button>", lambda e: display_loadout(spell_list, spell_loadout_label))
        btnLoad.grid(row=3, column=1, padx = 2, pady = 2)

        def display_loadout(spell_list, spell_loadout_label):
            for i in spell_list:
                spell_list.remove(i)
            sheet = filedialog.askopenfilename(initialdir = "./Sheets/SpellLoadouts/", title = "Select a File", filetypes = (("Text", "*.txt*"), ("all files",  "*.*")))
            if (str(sheet) != ''):
                temp = readCSV(sheet)
                for i in temp:
                    Add_Spell(i, spell_loadout_label)
            else:
                file_error()

        def prev_spell():
            
            spell_viewer = Toplevel(self)
            spell_viewer.title(spell_name.get())
            spell_viewer.geometry("400x400")
            spell_viewer.iconbitmap(r"The-Keep.ico")

            spell_viewer.configure(background=BgColor)

            spell_frame = Frame(spell_viewer)
            spell_frame.config()
            spell_frame.pack()

            for i in spells_:
                if (str(i.name) == selected_spell.get()):
                    lbl = Label(spell_frame, fg = "white smoke", background = BgColor, justify = "left", text = i.display().replace('*','\u2022'))
                    lbl.pack()

        btnPrev = Button(frame, bg=lblColor, fg="white smoke", text ="Preview Spell")
        btnPrev.bind("<Button>", lambda e: prev_spell())
        btnPrev.grid(row=3, column=4, padx = 2, pady = 2)
            
