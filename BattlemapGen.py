## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere

from KeepFunctions import *

class BattlemapGen(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("Battlemap Generator") 
        self.geometry("400x400")

        terrains = readCSV("./CSVs/TerrainTypes.txt")
        
        terrainTypes = StringVar()
        terrainTypes.set(terrains[0])

        opt = OptionMenu(self, terrainTypes, *terrains) ## drop down menu select
        opt.pack()

        def GenMap(*args):
            temp = 0
        
        button1 = Button(self, text="Generate", command=GenMap) 
        button1.pack()
