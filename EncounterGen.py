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
        self.geometry("400x400")

        monsterTypes = ["Humanoid","..."]

        terrains = readCSV("./CSVs/TerrainTypes.txt")
        
        terrainTypes = StringVar()
        terrainTypes.set(terrains[0])

        difficulties = ["Non-Combatant", "Fodder", "Tough_Guys", "Mid_Bosses", "Bosses"]
        
        difficulty = StringVar()
        difficulty.set(difficulties[0])
        
        terrains_label = Label(self, text ="Terrain")
        terrains_label.grid(row=1, column=0, padx = 2, pady = 2)
        terrains_entry = OptionMenu(self, terrain, *terrains) ## field for entry
        terrains_entry.grid(row=1, column=1, padx = 2, pady = 2)

        dif_label = Label(self, text ="Difficulty")
        dif_label.grid(row=1, column=2, padx = 2, pady = 2)
        dif_entry = OptionMenu(self, wis, *difficulties) ## field for entry
        dif_entry.grid(row=1, column=3, padx = 2, pady = 2)

        if (difficulty.get() == "Place"):
            pass
        elif (difficulty.get() == "Holder"):
            pass
