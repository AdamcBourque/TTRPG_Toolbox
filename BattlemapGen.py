## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere

from KeepFunctions import *
from perlin_noise import *
import matplotlib.pyplot as plt
import tkinter as tk


class BattlemapGen(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("Battlemap Generator") 
        self.geometry("800x300")

        terrains = readCSV("./CSVs/TerrainTypes.txt")
        features = readCSV("./CSVs/TerrainTypes.txt") ## temp
        sizes = ["Small","Medium","Large"]
        featureDensities = ["None","Low","Normal","High"]

        frame = Frame(self)
        frame.pack()
        
        terrainTypes = StringVar()
        terrainTypes.set(terrains[0])

        terrain_label = Label(frame, text ="Terrain Type")
        terrain_label.grid(row=1, column=0, padx = 2, pady = 2)
        TerrainOpt = OptionMenu(frame, terrainTypes, *terrains) ## drop down menu select
        TerrainOpt.grid(row=1, column=2, padx = 2, pady = 2)

        size = StringVar()
        size.set(sizes[0])

        size_label = Label(frame, text ="Size")
        size_label.grid(row=1, column=5, padx = 2, pady = 2)
        SizeOpt = OptionMenu(frame, size, *sizes) ## drop down menu select
        SizeOpt.grid(row=1, column=6, padx = 2, pady = 2)

        density = StringVar()
        density.set(featureDensities[2])

        density_label = Label(frame, text ="Feature Density")
        density_label.grid(row=1, column=7, padx = 2, pady = 2)
        DensityOpt = OptionMenu(frame, density, *featureDensities) ## drop down menu select
        DensityOpt.grid(row=1, column=8, padx = 2, pady = 2)

        new_frame = Frame(self)
        new_frame.pack()

        info_label = Label(new_frame, text ="Map may take some time to generate")
        info_label.pack()

        def GenMap(size, density, terrainType):
            ## Size choice
            if (size == 'Small'):
                xpix, ypix = 100, 100
            elif (size == 'Medium'):
                xpix, ypix = 200, 200
            elif (size == 'Large'):
                xpix, ypix = 300, 300
                
            ## Density choice
            if (density == 'None'):
                
            elif (density == 'Low'):
                
            elif (density == 'Normal'):
               
            elif (density == 'High'):
                
            octi = xpix/100
            noise = PerlinNoise(octaves = octi, seed = randint(1,8))
            
            ##Terrain Choice
            if (terrainType == 'Arctic'):
                color = 'Blues'
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
            elif (terrainType == 'Coastal'):
                color = 'YlGnBu'
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
            elif (terrainType == 'Desert'):
                color = 'Wistia'
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
            elif (terrainType == 'Forest'):
                color = 'YlGn'
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
            elif (terrainType == 'Grassland'):
                color = 'summer'
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
            elif (terrainType == 'Hill'):
                color = 'Greens'
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
            elif (terrainType == 'Mountain'):
                color = 'copper'
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
            elif (terrainType == 'Open Water'):
                color = 'winter'
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
            elif (terrainType == 'Swamp'):
                color = 'BrBG'
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
            elif (terrainType == 'Underdark'):
                color = 'bone'
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
            elif (terrainType == 'Underwater'):
                color = 'terrain'
                octi *= 2
                noise = PerlinNoise(octaves = octi, seed = randint(1,8))
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
            elif (terrainType == 'Urban'):
                color = 'binary'
                octi = 1
                noise = PerlinNoise(octaves = octi, seed = randint(1,8))
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]          

            plt.imshow(pic, cmap=color)
            plt.axis(False)
            plt.show()
        
        
        btnBattlemap = tk.Button(frame, text ="Generate")
        btnBattlemap.bind("<Button>", lambda e: GenMap(size.get(), density.get(), terrainTypes.get()))
        btnBattlemap.grid(row=1, column=9, padx = 2, pady = 2)
