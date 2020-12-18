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
        self.geometry("800x300")

        terrains = readCSV("./CSVs/TerrainTypes.txt")
        features = readCSV("./CSVs/TerrainTypes.txt") ## temp
        sizes = ["Small","Medium","Large"]
        featureDensities = ["None","Low","Normal","High"]
        
        terrainTypes = StringVar()
        terrainTypes.set(terrains[0])

        terrain_label = Label(self, text ="Terrain Type")
        terrain_label.grid(row=1, column=0, padx = 2, pady = 2)
        TerrainOpt = OptionMenu(self, terrainTypes, *terrains) ## drop down menu select
        TerrainOpt.grid(row=1, column=2, padx = 2, pady = 2)

        FeatureTypes = StringVar()
        FeatureTypes.set(features[0])

        feature_label = Label(self, text ="Feature Type")
        feature_label.grid(row=1, column=3, padx = 2, pady = 2)
        FeatureOpt = OptionMenu(self, terrainTypes, *terrains) ## drop down menu select
        FeatureOpt.grid(row=1, column=4, padx = 2, pady = 2)

        size = StringVar()
        size.set(sizes[0])

        size_label = Label(self, text ="Size")
        size_label.grid(row=1, column=5, padx = 2, pady = 2)
        SizeOpt = OptionMenu(self, size, *sizes) ## drop down menu select
        SizeOpt.grid(row=1, column=6, padx = 2, pady = 2)

        density = StringVar()
        density.set(featureDensities[2])

        density_label = Label(self, text ="Feature Density")
        density_label.grid(row=1, column=7, padx = 2, pady = 2)
        DensityOpt = OptionMenu(self, density, *featureDensities) ## drop down menu select
        DensityOpt.grid(row=1, column=8, padx = 2, pady = 2)


        def GenMap(*args):
            temp = 0
        
        button1 = Button(self, text="Generate", command=GenMap) 
        button1.grid(row=2, column=3, padx = 2, pady = 2)
