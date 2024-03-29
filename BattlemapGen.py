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
from random import choice


class BattlemapGen(Toplevel): 
      
    def __init__(self, Terrain): 
          
        super().__init__() 
        self.title("Battlemap Generator") 
        self.geometry("800x300")
        self.iconbitmap(r"The-Keep.ico")

        # set lable font
        lblFont = tkFont.Font(family='Helvetica', size=24, weight=tkFont.BOLD)
        btnFont = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)

        # sets bacckground color
        self.configure(background=BgColor)

        terrains = readCSV("./CSVs/TerrainTypes.txt")
        features = readCSV("./CSVs/TerrainTypes.txt") ## temp
        sizes = ["Small","Medium","Large"]
        featureDensities = ["None","Low","Normal","High"]

        frame = Frame(self)
        frame.config(bg=BgColor)
        frame.pack()

        map_name = StringVar()
        map_name.set("New Map")

        map_name_label = Label(frame, fg="white smoke", background=BgColor, text ="Map Name")
        map_name_label.grid(row=1, column=0, padx = 2, pady = 2)
        map_name_entry = Entry(frame, textvariable=map_name)
        map_name_entry.grid(row=2, column=0, padx = 2, pady = 2)
        
        terrainTypes = StringVar()
        terrainTypes.set(terrains[0])

        terrain_label = Label(frame, fg="white smoke", background=BgColor, text ="Terrain Type")
        terrain_label.grid(row=1, column=1, padx = 2, pady = 2)
        TerrainOpt = OptionMenu(frame, terrainTypes, *terrains) ## drop down menu select
        TerrainOpt.config(fg="white smoke", background=lblColor, highlightbackground = BgColor, highlightcolor = BgColor)
        TerrainOpt.grid(row=2, column=1, padx = 2, pady = 2)

        size = StringVar()
        size.set(sizes[0])

        size_label = Label(frame, fg="white smoke", background=BgColor, text ="Size")
        size_label.grid(row=1, column=2, padx = 2, pady = 2)
        SizeOpt = OptionMenu(frame, size, *sizes) ## drop down menu select
        SizeOpt.config(fg="white smoke", background=lblColor, highlightbackground = BgColor, highlightcolor = BgColor)
        SizeOpt.grid(row=2, column=2, padx = 2, pady = 2)

        density = StringVar()
        density.set(featureDensities[2])

        density_label = Label(frame, fg="white smoke", background=BgColor, text ="Feature Density")
        density_label.grid(row=1, column=3, padx = 2, pady = 2)
        DensityOpt = OptionMenu(frame, density, *featureDensities) ## drop down menu select
        DensityOpt.config(fg="white smoke", background=lblColor, highlightbackground = BgColor, highlightcolor = BgColor)
        DensityOpt.grid(row=2, column=3, padx = 2, pady = 2)

        new_frame = Frame(self)
        new_frame.config(bg=BgColor)
        new_frame.pack()

        info_label = Label(new_frame, fg="white smoke", background=BgColor, text ="Map may take some time to generate")
        info_label.pack()

        xpix, ypix = 100, 100

        def GenMap(size, density, terrainType):
            ## Size choice
            sizey = 400
            sizex = 462
            if (size == 'Small'):
                sizey = 400
                sizex = 462
            elif (size == 'Medium'):
                sizey = 800
                sizex = 924
            elif (size == 'Large'):
                sizey = 1200
                sizex = 1386
                
            ## Density choice
            densityv = 10000
            if (density == 'None'):
                densityv=0
            elif (density == 'Low'):
                densityv=2*sizey/100
            elif (density == 'Normal'):
                densityv=4*sizey/100
            elif (density == 'High'):
                densityv=8*sizey/100
                
            octi = xpix/100
            noise = PerlinNoise(octaves = octi, seed = randint(1,8))
            color = 'Blues'
            pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
            resourcePath = "./Resources/ArcticResources/"
            
            ##Terrain Choice
            if (terrainType == 'Arctic'):
                color = 'Blues'
                pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
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

            saveToCsv()

            dx, dy = 0.05, 0.05

            x = np.arange(0.0, 5.0, dx)
            y = np.arange(0.0, 5.0, dy)
            X, Y = np.meshgrid(x, y)

            extent = np.min(x), np.max(x), np.min(y), np.max(y)
            fig = plt.figure()
            fig.set_size_inches(sizex/100,sizey/100)

            
            im1 = plt.imshow(pic, cmap=color, interpolation='hanning',
                 extent=extent)
            
            
            plt.axis(False)
            fig.savefig("./Maps/" + map_name.get() + ".png", bbox_inches='tight', pad_inches = 0)

            first_image = PIL.Image.open("./Maps/" + map_name.get() + ".png")
            first_image = first_image.resize((sizex,sizey), resample=0)

            for i in range(0,int(sizey/50)):
                for j in range(0,int(sizey/50)):
                    check = randint(0,int(sizex/50*sizey/50))
                    if (check < densityv):
                        second_image = PIL.Image.open(resourcePath + choice(listdir(resourcePath)))
                        second_image = second_image.resize((50,50), resample=0)
                        first_image.paste(second_image, (i*50+6,j*50+6), mask = second_image)
            
            first_image.show()
            first_image.save("./Maps/" + map_name.get() + ".png")
            

                    
        
        btnBattlemap = tk.Button(frame,  fg="white smoke", background=lblColor, text ="Generate")
        btnBattlemap.bind("<Button>", lambda e: GenMap(size.get(), density.get(), terrainTypes.get()))
        btnBattlemap.grid(row=2, column=4, padx = 2, pady = 2)

        def loadParams():
            if (str(Terrain) != "Keep"):
                terrainTypes.set(str(Terrain))
                if (str(Terrain) != "Type"):
                    GenMap(size.get(), density.get(), str(terrainTypes.get()))

        def saveToCsv():
            output = ""  ## holds the fields in the form of a csv
            output += terrainTypes.get() + ""
                
            sheet = open("./MapData/" + map_name.get() + ".txt", "w") ## writes output to file "name.txt"
            output = output.replace('\ufeff', '')
            sheet.write(output)
            sheet.close()

        loadParams()
