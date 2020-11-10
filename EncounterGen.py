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

        terrains = readCSV("./CSVs/TerrainTypes.txt")
        
        terrainTypes = StringVar()
        terrainTypes.set(terrains[0])
        
        label = Label(self, text ="This is a new Window")
        label.pack(fill = X, padx=5, pady=5)
