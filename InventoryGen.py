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
        self.geometry("400x650")
        
        shops = readCSV("./CSVs/ShopTypes.txt") ## list of shop types

        economic_levels = ["Wealthy", "Comfortable", "Modest", "Poor", "Squalid"] ## list of wealth categories 
        
        shopTypes = StringVar()  ## currently selected shop
        shopTypes.set(shops[0])  

        opt = OptionMenu(self, shopTypes, *shops) ## drop down menu select
        opt.pack()

        economic_level = StringVar()
        economic_level.set(economic_levels[2])

        eco_opt = OptionMenu(self, economic_level, *economic_levels) ## drop down menu select
        eco_opt.pack()

        output = StringVar()
        
        label = Label(self, textvariable = output)

        def GenInventory(*args):
            fish = shopTypes.get()
            fish = fish.replace("\ufeff", '')
            shop = ("./CSVs/Inventories/" + fish + "Inventory.txt") ## file path of inventory csv for selected shop
            items = readTupleCSV(shop) ## list of Items
            rarity = {'C':75, 'U':50, 'R':25, 'V':10, 'L':1} ## rarity to quantity dictionary
            economic_multiplier = {"Wealthy":2.5, "Comfortable":1.5, "Modest":1, "Poor":.5, "Squalid":.25}
            temp = 0
            count = 0
            string = ''
            

            for i in items:
                temp = randint(0,100)
                multi = economic_multiplier[economic_level.get()]

                if (count < 25):
                    if (temp < rarity[i[1]] * multi):
                        q = (rarity[i[1]] / 10) * multi
                        q = int(ceil(q))
                        if (i[1] == 'L'):
                            q = 1
                        string += (i[0] + ": " + str(q) + " - " + i[2] + "\n")
                        count = count + 1
                    
                
            output.set(string)
            label.pack()
            
        button1 = Button(self, text="Generate", command=GenInventory) 
        button1.pack()
