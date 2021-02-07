## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere

from KeepFunctions import *
from perlin_noise import *
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import matplotlib.image as mpimg
import PIL as PIL
from os import listdir
from random import choice


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

        map_name = StringVar()
        map_name.set("New Map")

        map_name_label = Label(frame, text ="Terrain Type")
        map_name_label.grid(row=1, column=0, padx = 2, pady = 2)
        map_name_entry = Entry(frame, textvariable=map_name)
        map_name_entry.grid(row=1, column=2, padx = 2, pady = 2)
        
        terrainTypes = StringVar()
        terrainTypes.set(terrains[0])

        terrain_label = Label(frame, text ="Terrain Type")
        terrain_label.grid(row=1, column=3, padx = 2, pady = 2)
        TerrainOpt = OptionMenu(frame, terrainTypes, *terrains) ## drop down menu select
        TerrainOpt.grid(row=1, column=4, padx = 2, pady = 2)

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

        xpix, ypix = 100, 100

        def GenMap(size, density, terrainType):
            ## Size choice
            size = 400
            if (size == 'Small'):
                size = 400
            elif (size == 'Medium'):
                size = 800
            elif (size == 'Large'):
                size = 1200
                
            ## Density choice
            densityv = 10000
            if (density == 'None'):
                densityv=0
            elif (density == 'Low'):
                densityv=2*size/100
            elif (density == 'Normal'):
                densityv=4*size/100
            elif (density == 'High'):
                densityv=8*size/100
                
            octi = xpix/100
            noise = PerlinNoise(octaves = octi, seed = randint(1,8))
            color = 'Blues'
            pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
            resourcePath = "./Resources/ArcticResources/"
            
            ##Terrain Choice
            if (terrainType == 'Arctic'):
                color = 'Blues'
                pic = [[noise([i/xpix, j/ypix]/5) for j in range(xpix)] for i in range(ypix)]
                resourcePath = "./Resources/ArcticResources/"
            elif (terrainType == 'Coastal'):
                color = 'YlGnBu'
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
                resourcePath = "./Resources/CoastalResources/"
            elif (terrainType == 'Desert'):
                color = 'Wistia'
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
                resourcePath = "./Resources/DesertResources/"
            elif (terrainType == 'Forest'):
                color = 'YlGn'
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
                resourcePath = "./Resources/ForestResources/"
            elif (terrainType == 'Grassland'):
                color = 'summer'
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
                resourcePath = "./Resources/GrasslandResources/"
            elif (terrainType == 'Hill'):
                color = 'Greens'
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
                resourcePath = "./Resources/HillResources/"
            elif (terrainType == 'Mountain'):
                color = 'copper'
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
                resourcePath = "./Resources/MountainResources/"
            elif (terrainType == 'Open Water'):
                color = 'winter'
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
                resourcePath = "./Resources/OpenWaterResources/"
            elif (terrainType == 'Swamp'):
                color = 'BrBG'
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
                resourcePath = "./Resources/SwampResources/"
            elif (terrainType == 'Underdark'):
                color = 'bone'
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
            elif (terrainType == 'Underwater'):
                color = 'terrain'
                octi *= 2
                noise = PerlinNoise(octaves = octi, seed = randint(1,8))
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
                resourcePath = "./Resources/UnderwaterResources/"
            elif (terrainType == 'Urban'):
                color = 'binary'
                octi = 1
                noise = PerlinNoise(octaves = octi, seed = randint(1,8))
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
                resourcePath = "./Resources/UrbanResources/"

            dx, dy = 0.05, 0.05

            x = np.arange(0.0, 5.0, dx)
            y = np.arange(0.0, 5.0, dy)
            X, Y = np.meshgrid(x, y)

            extent = np.min(x), np.max(x), np.min(y), np.max(y)
            fig = plt.figure()
            fig.set_size_inches(6,6)

            
            im1 = plt.imshow(pic, cmap=color, interpolation='hanning',
                 extent=extent)
            
            
            plt.axis(False)
            fig.savefig(map_name.get() + ".png", bbox_inches='tight')

            first_image = PIL.Image.open(map_name.get() + ".png")
            first_image = first_image.resize((size,size), resample=0)

            for i in range(0,int(size/50)):
                for j in range(0,int(size/50)):
                    check = randint(0,int(size/50*size/50))
                    if (check < densityv):
                        second_image = PIL.Image.open(resourcePath + choice(listdir(resourcePath)))
                        second_image = second_image.resize((50,50), resample=0)
                        first_image.paste(second_image, (i*50,j*50), mask = second_image)
            
            first_image.show()
            first_image.save(map_name.get() + ".png")
            

            
        
        
        btnBattlemap = tk.Button(frame, text ="Generate")
        btnBattlemap.bind("<Button>", lambda e: GenMap(size.get(), density.get(), terrainTypes.get()))
        btnBattlemap.grid(row=1, column=9, padx = 2, pady = 2)
