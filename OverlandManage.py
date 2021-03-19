## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere

from KeepFunctions import *
import math
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np
import PIL as PIL
import tkinter as tk
from EncounterGen import *

class OverlandManage(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("New Window") 
        self.geometry("800x600")
        
        terrains = readCSV("./CSVs/TerrainTypes.txt")
        features = readCSV("./CSVs/TerrainTypes.txt") ## temp
        sizes = ["Small","Medium","Large"]
        maps = listdir("./Maps")

        frame = Frame(self)
        frame.pack()

        map_name = StringVar()
        map_name.set("New Map")

        map_name_label = Label(frame, text ="Map Name")
        map_name_label.grid(row=1, column=0, padx = 2, pady = 2)
        map_name_entry = OptionMenu(frame, map_name, *maps) ## drop down menu select
        map_name_entry.grid(row=1, column=2, padx = 2, pady = 2)
        
        terrainTypes = StringVar()
        terrainTypes.set(terrains[0])

        size = IntVar()
        size.set(25)

        size_label = Label(frame, text ="Size")
        size_label.grid(row=1, column=5, padx = 2, pady = 2)

        def Csize(_=None):
            size.set(SizeOpt.get())
            
        SizeOpt = Scale(frame, orient = HORIZONTAL, from_=25, to=75, resolution=1, command = Csize)
        
        SizeOpt.grid(row=1, column=6, padx = 2, pady = 2)

        text = 0


        def overlay():
            
            
            ## Size choice
            size_hex = size.get()
            global offCoord, text

            def generate_unit_hexagons(image_width, image_height):
                """Generate coordinates for a tiling of unit hexagons."""
                # Half the height of the hexagon
                h = math.sin(math.pi / 3)

                for x in range(0, round(image_width / ((3 / 4) * (size_hex / 25) * math.sqrt(3)))):  # x is the x coordinate moving by 1
                    for y in range(0, round(image_height / ((4 / 7) * size_hex / 25)) + round(6 / (size_hex/25))): # y is the y coordinate moving by 1

                        # Add the horizontal offset on every other row
                        x_ = 2*x if (y % 2 == 0) else 2*x + 1
                            
                        
                        offCoord.append([x_,y])

            offCoord = [] ## locations of hexes

            hex_img = PIL.Image.open("hex.png") # hex tile

            first_image = PIL.Image.open("./Maps/" + map_name.get()) # The map

            sizeX = first_image.size[0]
            sizeY = first_image.size[1]

            generate_unit_hexagons(sizeX/25, sizeY/25)

            print(len(offCoord))

            saveToCsv()

            for c in offCoord:
                hex_img = hex_img.resize((size_hex,size_hex), resample=1) # size of hexes
                margin = round(size_hex/4)
                if (round(c[0]*18*size_hex/25) < sizeX or round(c[1]*12*size_hex/25) < sizeY):
                    first_image.paste(hex_img, (round(c[0]*18*size_hex/25), round(c[1]*12*size_hex/25)), mask = hex_img) # place of hex

                    text = text + 1
                
                    draw = ImageDraw.Draw(first_image)  

                    x = round(c[0]*18*size_hex/25) + margin
                    y = round(c[1]*12*size_hex/25) + margin
                
                    draw.text((x, y), str(text))

            first_image.show()
            first_image.save("./Maps/" + map_name.get() + ".png")

        btnOverlay = Button(frame, text ="Generate")
        btnOverlay.bind("<Button>", lambda e: overlay())
        btnOverlay.grid(row=1, column=9, padx = 2, pady = 2)

        btnEncounter = Button(frame, text ="Generate Encounter")
        btnEncounter.bind("<Button>", lambda e: EncounterGen(self))
        btnEncounter.grid(row=2, column=9, padx = 2, pady = 2)

        def submit():
            print("tested")

        def tile_formatter():
            global terrainTypes, terrains, tiles
            
            formatter = Toplevel(self)
            formatter.title("Test")
            formatter.geometry("200x200")

            terrain_label = Label(formatter, text ="Terrain Type")
            terrain_label.grid(row=1, column=3, padx = 2, pady = 2)
            TerrainOpt = OptionMenu(formatter, terrainTypes, *terrains) ## drop down menu select
            TerrainOpt.grid(row=1, column=4, padx = 2, pady = 2)

            btnSubmit = Button(formatter, text ="Submit")
            btnSubmit.bind("<Button>", lambda e: submit())
            btnSubmit.grid(row=1, column=9, padx = 2, pady = 2)

        tiles = []
        for i in range(1,text):
            tiles.append(i)


        range_start = IntVar()
        range_start.set(1)
        range_end = IntVar()
        range_end.set(1)

        range_start_label = Label(frame, text ="Tile Start")
        range_start_label.grid(row=2, column=3, padx = 2, pady = 2)
        range_start_entry = Entry(frame, textvariable = range_start)
        range_start_entry.grid(row=2, column=4, padx = 2, pady = 2)

        range_end_label = Label(frame, text ="Tile End")
        range_end_label.grid(row=2, column=5, padx = 2, pady = 2)
        range_end_entry = Entry(frame, textvariable = range_end)
        range_end_entry.grid(row=2, column=6, padx = 2, pady = 2)

        btnEncounter = Button(frame, text ="Format Tiles")
        btnEncounter.bind("<Button>", lambda e: tile_formatter())
        btnEncounter.grid(row=2, column=7, padx = 2, pady = 2)

        def saveToCsv():
            global offCoord
            output = ""  ## holds the fields in the form of a csv
            output += map_name.get() + ","
            output += terrainTypes.get() + ","
            output += str(size.get()) + ""
                
            sheet = open("./MapData/" + map_name.get() - ".png" + ".txt", "w") ## writes output to file "name.txt"
            output = output.replace('\ufeff', '')
            sheet.write(output)
            sheet.close()
      
        
        


        
