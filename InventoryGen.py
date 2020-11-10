## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere

from KeepFunctions import *

class ShopInventory(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("Shop Inventory Generator") 
        self.geometry("400x400")
        
        shops = readCSV("./CSVs/ShopTypes.txt") ## list of shop types
        
        shopTypes = StringVar()  ## currently selected shop
        shopTypes.set(shops[0])  

        opt = OptionMenu(self, shopTypes, *shops) ## drop down menu select
        opt.pack()

        def GenInventory(*args):
            fish = shopTypes.get()
            fish = fish.replace("\ufeff", '')
            shop = ("./CSVs/" + fish + "Inventory.txt") ## file path of inventory csv for selected shop
            items = readTupleCSV(shop) ## list of Items
            rarity = {'C':(10,30), 'U':(5,10), 'R':(1,5), 'V':(0,1), 'L':(0,1)} ## rarity to quantity dictionary
            temp = ""
            output = StringVar()

            for i in items:
                temp += (i[0] + ": " + str(randint(rarity[i[1]][0],rarity[i[1]][1])) + " - " + i[2] + "\n")

            output.set(temp)
            label = Label(self, textvariable = output)
            label.pack()
            
        button1 = Button(self, text="Generate", command=GenInventory) 
        button1.pack()
