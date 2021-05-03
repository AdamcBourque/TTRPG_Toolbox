## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere

from KeepFunctions import *

terrains = []

class EncounterGen(Toplevel): 
      
    def __init__(self, Terrain, Diff, Quant):
          
        super().__init__() 
        self.title("Encounter Generator") 
        self.geometry("800x400")

        global terrains

        monsterTypes = ["Humanoid","..."]

        terrains = readCSV("./CSVs/TerrainTypes.txt")
        for q in terrains:
            q.replace("\ufeff",'')
        print(terrains[0])
        
        terrainTypes = StringVar()
        terrainTypes.set(terrains[0])

        frame = Frame(self)
        frame.pack()

        output_frame = Frame(self)
        output_frame.pack()

        difficulties = ["Non-Combatant", "Fodder", "Tough_Guys", "Mid_Bosses", "Bosses"]
        mobs = [1,2,3,4,5,6]
        
        difficulty = StringVar()
        difficulty.set(difficulties[0])

        terrains_label = Label(frame, text ="Terrain")
        terrains_label.grid(row=1, column=3, padx = 2, pady = 2)
        terrains_entry = OptionMenu(frame, terrainTypes, *terrains) ## field for entry
        terrains_entry.grid(row=1, column=4, padx = 2, pady = 2)

        dif_label = Label(frame, text ="Difficulty")
        dif_label.grid(row=1, column=5, padx = 2, pady = 2)
        dif_entry = OptionMenu(frame, difficulty, *difficulties) ## field for entry
        dif_entry.grid(row=1, column=6, padx = 2, pady = 2)

        Label_Encounter = Label(output_frame, text = "")
        Label_Encounter.grid(row=0, column=0, padx = 2, pady = 2)

        number_enemies = StringVar()
        number_enemies.set(mobs[0])

        number_enemies_label = Label(frame, text ="Number of Enemies")
        number_enemies_label.grid(row=1, column=7, padx = 2, pady = 2)
        number_enemies_entry = OptionMenu(frame, number_enemies, *mobs) ## field for entry
        number_enemies_entry.grid(row=1, column=8, padx = 2, pady = 2)
        

        def loadParams():
            if (Terrain != "Keep"):
                terrainTypes.set(Terrain)
                difficulty.set(Diff)
                number_enemies.set(Quant)
                GenEncounter()
        
        def GenEncounter():
            global terrains
            terrains[0] = terrains[0].replace("\ufeff", '')
            Enemies = []
            Master = readTupleCSV2("./CSVs/EncountersMaster.txt")
            final_drops = []
            terrain_check = terrains.index(terrainTypes.get().replace("\ufeff",'')) + 1

            
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
                Master[i] = Master[i].replace("(", "").replace(")",'')
                temp = Master[i].split(",")
                Cr = float(temp[-2])

                if (Cr >= floor and Cr <= cap and int(temp[terrain_check]) == 1):
                    Enemies.append([temp[0],temp[-1],temp[-2]])
                
            output = ''
            for i in range (0,int(number_enemies.get())):
                encounter = selectFromList(Enemies)
                encounter_string = encounter[0] + " CR: " + encounter[2] + " Creature Type: " + encounter[1]

                Drops = readTupleCSV2("./CSVs/Loot/" + encounter[1] + "Loot.txt")
                legendary = []
                veryRare = []
                rare = []
                uncommon = []
                common = []

                for j in range (0, len(Drops)):
                    Drops[j] = Drops[j].replace("(", "").replace(")",'')
                    temp = Drops[j].split(",")
                    item = temp[1]
                    
                    if (temp[0] == 'L'):
                        legendary.append("Drops: " + item)
                    elif (temp[0] == 'V'):
                        veryRare.append("Drops: " + item)
                    elif (temp[0] == 'R'):
                        rare.append("Drops: " + item)
                    elif (temp[0] == 'U'):
                        uncommon.append("Drops: " + item)
                    else:
                        common.append("Drops: " + item)
                        
                
                populated = False
                while(not populated):
                    rarity = randint(0,100)
                    if (rarity > 96):
                        if (len(legendary) != 0):
                            drop_string = selectFromList(legendary)
                            populated = True
                    elif (rarity > 89):
                        if (len(veryRare) != 0):
                            drop_string = selectFromList(veryRare)
                            populated = True
                    elif (rarity > 75):
                        if (len(rare) != 0):
                            drop_string = selectFromList(rare)
                            populated = True
                    elif (rarity > 50):
                        if (len(uncommon) != 0):
                            drop_string = selectFromList(uncommon)
                            populated = True
                    else:
                        if (len(common) != 0):
                            drop_string = selectFromList(common)
                            populated = True
                    
                output += encounter_string + '\n' + drop_string + '\n' + "---------------------------------" + '\n'
                
            Label_Encounter.config(text = output) 

        btnGen = Button(frame, text ="Generate")
        btnGen.bind("<Button>", lambda e: GenEncounter())
        btnGen.grid(row=2, column=9, padx = 2, pady = 2)

        loadParams()
