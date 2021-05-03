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


terrains = []
tiles = []
text = 0
formatter = []
data = []

class OverlandManage(Toplevel): 
      
    def __init__(self, master = None):

        global terrains
        global formatter
        terrains = readCSV("./CSVs/TerrainTypes.txt")
        chance = StringVar()
          
        super().__init__(master = master) 
        self.title("Overland Travel Manager") 
        self.geometry("800x600")
        
        features = readCSV("./CSVs/TerrainTypes.txt") ## temp
        sizes = ["Small","Medium","Large"]
        difficulties = ["Non-Combatant", "Fodder", "Tough_Guys", "Mid_Bosses", "Bosses"]
        maps = listdir("./Maps")

        frame = Frame(self)
        frame.pack()

        lbl_frame = Frame(self)
        lbl_frame.pack()

        map_name = StringVar()
        map_name.set("New Map")

        map_name_label = Label(frame, text ="Map Name")
        map_name_label.grid(row=1, column=0, padx = 2, pady = 2)
        map_name_entry = OptionMenu(frame, map_name, *maps) ## drop down menu select
        map_name_entry.grid(row=1, column=2, padx = 2, pady = 2)
        
        terrainTypes = StringVar()
        terrainTypes.set(terrains[0])

        difficulty = StringVar()
        difficulty.set(difficulties[0])

        quant = StringVar()
        quant.set("1")
        mobs = [1,2,3,4,5,6]

        size = IntVar()
        size.set(25)

        size_label = Label(frame, text ="Size")
        size_label.grid(row=1, column=5, padx = 2, pady = 2)

        def Csize(_=None):
            size.set(SizeOpt.get())
            
        SizeOpt = Scale(frame, orient = HORIZONTAL, from_=25, to=75, resolution=1, command = Csize)
        
        SizeOpt.grid(row=1, column=6, padx = 2, pady = 2)

        btnLoad = Button(frame, text ="Load")
        btnLoad.bind("<Button>", lambda e: loadFromCsv())
        btnLoad.grid(row=1, column=7, padx = 2, pady = 2)

        hex_id = StringVar()
        hex_id.set(0)
        
        hex_id_label = Label(frame, text ="Hex ID")
        hex_id_label.grid(row=2, column=0, padx = 2, pady = 2)
        hex_id_entry = Entry(frame, textvariable = hex_id)
        hex_id_entry.grid(row=2, column=1, padx = 2, pady = 2)

        btnCheck = Button(frame, text ="Check for Encounter")
        btnCheck.bind("<Button>", lambda e: check())
        btnCheck.grid(row=2, column=5, padx = 2, pady = 2)

        lbl_encounter = Label(lbl_frame, text = '')
        lbl_encounter.pack()
        

        def check():
            global formatter
            lbl_encounter.config(text = '')
            num = randint(0,100)
            tile = formatter[int(hex_id.get())]
            if (num < int(data[2+5*int(hex_id.get())])):
                EncounterGen(tile[1], tile[2], tile[3])
            else:
                lbl_encounter.config(text = "No encounter for this hex.")

        def overlay():
            ## Size choice
            size_hex = size.get()
            global offCoord, text
            text = 0
            
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

            ##saveToCsv()

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

                    formatter.append([text, "Type" , "Challenge Level", "Enemies", 0])

            first_image.show()
            first_image.save("./Maps/HexMaps/" + map_name.get())
            btnFormatter.grid(row=2, column=7, padx = 2, pady = 2)

        btnOverlay = Button(frame, text ="Generate")
        btnOverlay.bind("<Button>", lambda e: overlay())
        btnOverlay.grid(row=1, column=9, padx = 2, pady = 2)

        btnEncounter = Button(frame, text ="Generate Encounter")
        btnEncounter.bind("<Button>", lambda e: EncounterGen("Keep", 0, 0))
        btnEncounter.grid(row=2, column=9, padx = 2, pady = 2)

        def submit(name, start, end):
            global formatter
            for i in range (start-1, end):
                formatter[i][1] = terrainTypes.get().replace("\ufeff", "")
                formatter[i][2] = difficulty.get()
                formatter[i][3] = quant.get()
                formatter[i][4] = chance.get()
                
            saveToCsv(formatter)
            

        def tile_formatter(map_name):
            global terrains, text, formatter
            
            if (len(formatter) == 0):
                for i in range (0,int(text)):
                    formatter.append([i+1, "Type" , "Challenge Level", "Enemies", 0])
            
            formatterT = Toplevel(self)
            formatterT.title("Tile Formatter")
            formatterT.geometry("800x300")

            terrain_label = Label(formatterT, text ="Terrain Type")
            terrain_label.grid(row=1, column=3, padx = 2, pady = 2)
            TerrainOpt = OptionMenu(formatterT, terrainTypes, *terrains) ## drop down menu select
            TerrainOpt.grid(row=1, column=4, padx = 2, pady = 2)

            dif_label = Label(formatterT, text ="Difficulty")
            dif_label.grid(row=1, column=5, padx = 2, pady = 2)
            dif_entry = OptionMenu(formatterT, difficulty, *difficulties) ## field for entry
            dif_entry.grid(row=1, column=6, padx = 2, pady = 2)

            number_enemies_label = Label(formatterT, text ="Number of Enemies")
            number_enemies_label.grid(row=1, column=7, padx = 2, pady = 2)
            number_enemies_entry = OptionMenu(formatterT, quant, *mobs) ## field for entry
            number_enemies_entry.grid(row=1, column=8, padx = 2, pady = 2)

            chance_label = Label(formatterT, text ="% Chance")
            chance_label.grid(row=1, column=9, padx = 2, pady = 2)
            chance_entry = Entry(formatterT, textvariable = chance) ## field for entry
            chance_entry.grid(row=1, column=10, padx = 2, pady = 2)

            range_start = IntVar()
            range_start.set(1)
            range_end = IntVar()
            range_end.set(1)

            range_start_label = Label(formatterT, text ="Tile Start")
            range_start_label.grid(row=2, column=3, padx = 2, pady = 2)
            range_start_entry = Entry(formatterT, textvariable = range_start)
            range_start_entry.grid(row=2, column=4, padx = 2, pady = 2)

            range_end_label = Label(formatterT, text ="Tile End")
            range_end_label.grid(row=2, column=5, padx = 2, pady = 2)
            range_end_entry = Entry(formatterT, textvariable = range_end)
            range_end_entry.grid(row=2, column=6, padx = 2, pady = 2)

            btnSubmit = Button(formatterT, text ="Submit")
            btnSubmit.bind("<Button>", lambda e: submit(map_name, range_start.get(), range_end.get()))
            btnSubmit.grid(row=2, column=10, padx = 2, pady = 2)

        btnFormatter = Button(frame, text ="Format Tiles")
        btnFormatter.bind("<Button>", lambda e: tile_formatter(map_name.get()))

        def loadFromCsv():
            global text, formatter, data
            sheet = filedialog.askopenfilename(initialdir = "./MapData/", title = "Select a File", filetypes = (("Text", "*.txt*"), ("all files",  "*.*")))
            data = readCSV(sheet)
            map_name.set(data[0])
            terrainTypes.set(data[1])
            text = data[2]
            print("The fucked part: " + data[3])
            formatter = []
            for i in range (0,int(text),5):
                formatter.append([i/5+1, data[4+i] , data[5+i], data[6+i], data[7+i]])
            btnFormatter.grid(row=2, column=7, padx = 2, pady = 2)

        def saveToCsv(formatting):
            global offCoord, data
            global formatter
            output = ""  ## holds the fields in the form of a csv
            output += map_name.get() + ","
            output += terrainTypes.get() + ","
            output += str(text) + ","
            for tile in formatter:
                for i in tile:
                    output += str(i) + ","
            output.strip(",")
                
            sheet = open("./MapData/" + map_name.get().replace(".png", "") + ".txt", "w") ## writes output to file "name.txt" //////////////////////////////////////////////////
            output = output.replace('\ufeff', '')
            sheet.write(output)
            data = readCSV("./MapData/" + map_name.get().replace(".png", "") + ".txt")
            sheet.close()
            

      
        
        


        
