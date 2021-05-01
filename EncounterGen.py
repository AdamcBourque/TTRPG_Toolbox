## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere

from KeepFunctions import *

class EncounterGen(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("Encounter Generator") 
        self.geometry("800x400")

        monsterTypes = ["Humanoid","..."]

        terrains = readCSV("./CSVs/TerrainTypes.txt")
        
        terrainTypes = StringVar()
        terrainTypes.set(terrains[0])

        difficulties = ["Non-Combatant", "Fodder", "Tough_Guys", "Mid_Bosses", "Bosses"]
        
        difficulty = StringVar()
        difficulty.set(difficulties[0])

        maps = listdir("./MapData")

        map_name = StringVar()
        map_name.set(maps[0])

        map_name_label = Label(self, text ="Map Name")
        map_name_label.grid(row=1, column=0, padx = 2, pady = 2)
        map_name_entry = OptionMenu(self, map_name, *maps)
        map_name_entry.grid(row=1, column=1, padx = 2, pady = 2)
        
        terrains_label = Label(self, text ="Terrain")
        terrains_label.grid(row=1, column=3, padx = 2, pady = 2)
        terrains_entry = OptionMenu(self, terrainTypes, *terrains) ## field for entry
        terrains_entry.grid(row=1, column=4, padx = 2, pady = 2)

        dif_label = Label(self, text ="Difficulty")
        dif_label.grid(row=1, column=5, padx = 2, pady = 2)
        dif_entry = OptionMenu(self, difficulty, *difficulties) ## field for entry
        dif_entry.grid(row=1, column=6, padx = 2, pady = 2)

        Label_Encounter = Label(self, text = "")
        Label_Encounter.grid(row=3, column=1, padx = 2, pady = 2)

        def loadFromCsv():
            filename = filedialog.askopenfilename(initialdir = "./MapData", title = "Select a File", filetypes = (("Text", "*.txt*"), ("all files",  "*.*")))
            data = readCSV(filename)  ## reads in the data frome the csv selected above
            terrainTypes.set(data[1])

        
        def GenEncounter():
            Enemies = []
            Master = readTupleCSV2("./CSVs/EncountersMaster.txt")
            final_drops = []

            
            cap = 30
            floor = 0

            if (difficulty.get() == "Non-Combatant"):
                floor = 0
                cap = 2
            elif (difficulty.get() == "Fodder"):
                floor = 2
                cap = 4
            elif (difficulty.get() == "Tough_Guys"):
                floor = 4
                cap = 8
            elif (difficulty.get() == "Mid_Bosses"):
                floor = 8
                cap = 17
            elif (difficulty.get() == "Bosses"):
                floor = 17
                cap = 30
                
            for i in range (0, len(Master)):
                Master[i] = Master[i].replace("(", "")
                temp = Master[i].split(",")
                Cr = int(temp[-2])
            

                if (Cr >= floor and Cr <= cap):
                    Enemies.append([temp[0],temp[-1],temp[-2]])
                
                
            encounter = selectFromList(Enemies)
            encounter_string = encounter[0] + " CR: " + encounter[2] + " Creature Type: " + encounter[1]

            Drops = readTupleCSV2("./CSVs/Loot/" + encounter[1].replace(')','') + "Loot.txt")

            for i in range (0, len(Drops)):
                Drops[i] = Drops[i].replace("(", "")
                temp = Drops[i].split(",")
                rarity = temp[0]
                item = temp[1]
                final_drops.append("Drops: " + item)

            Label_Encounter.config(text = encounter_string + '\n' + selectFromList(final_drops)) 

        btnLoad = Button(self, text ="Load Map Data")
        btnLoad.bind("<Button>", lambda e: loadFromCsv())
        btnLoad.grid(row=1, column=7, padx = 2, pady = 2)

        btnGen = Button(self, text ="Generate")
        btnGen.bind("<Button>", lambda e: GenEncounter())
        btnGen.grid(row=2, column=7, padx = 2, pady = 2)
