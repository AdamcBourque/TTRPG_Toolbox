## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere

from KeepFunctions import *

class ShopInventory(Toplevel): 
      
    def __init__(self, master = None): 

        
          
        super().__init__(master = master) 

        # set label font
        lblFont = tkFont.Font(family='Helvetica', size=24, weight=tkFont.BOLD)
        btnFont = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)

        # sets background color
        self.configure(background=BgColor)

        self.title("Shop Inventory Generator") 
        self.geometry("400x650")
        self.iconbitmap(r"The-Keep.ico")
        
        shops = readCSV("./CSVs/ShopTypes.txt") ## list of shop types

        economic_levels = ["Wealthy", "Comfortable", "Modest", "Poor", "Squalid"] ## list of wealth categories 
        
        shopTypes = StringVar()  ## currently selected shop
        shopTypes.set(shops[0])

        frame = Frame(self)
        frame.config(bg = BgColor)
        frame.pack()

        lblfrme = Frame(self)
        lblfrme.config(bg = BgColor)
        lblfrme.pack()

        opt_label = Label(frame, fg="white smoke", background=BgColor, text ="Shop Type")
        opt_label.grid(row=1, column=0, padx = 2, pady = 2)
        opt = OptionMenu(frame, shopTypes, *shops) ## drop down menu select
        opt.config(fg="white smoke", background=lblColor, highlightbackground = BgColor, highlightcolor = BgColor)
        opt.grid(row=2, column=0, padx = 2, pady = 2)

        economic_level = StringVar()
        economic_level.set(economic_levels[2])

        eco_label = Label(frame, fg="white smoke", background=BgColor, text ="Economic Level")
        eco_label.grid(row=1, column=1, padx = 2, pady = 2)
        eco_opt = OptionMenu(frame, economic_level, *economic_levels) ## drop down menu select
        eco_opt.config(fg="white smoke", background=lblColor, highlightbackground = BgColor, highlightcolor = BgColor)
        eco_opt.grid(row=2, column=1, padx = 2, pady = 2)

        output = StringVar()
        output.set('\n' + "===== INVENTORY =====" + '\n' + "Item: Quantity - Price" + '\n' + '\n')
        
        label = Label(lblfrme, fg="white smoke", background=BgColor, textvariable = output)
        label.grid(row=1, column=6, padx = 2, pady = 2)

        def GenInventory(*args):
            fish = shopTypes.get()
            fish = fish.replace("\ufeff", '')
            shop = ("./CSVs/Inventories/" + fish + "Inventory.txt") ## file path of inventory csv for selected shop
            items = readTupleCSV(shop) ## list of Items
            shuffle(items)
            rarity = {'C':75, 'U':50, 'R':25, 'V':10, 'L':1} ## rarity to quantity dictionary
            economic_multiplier = {"Wealthy":2.5, "Comfortable":1.5, "Modest":1, "Poor":.5, "Squalid":.25}
            temp = 0
            count = 0
            
            
            if (fish == 'Magic Item Shop'):
                string = '\n' + "===== INVENTORY =====" + '\n' + "Item: Quantity - Requires Attunement (From Source)" + '\n' + '\n'
                attune = ''
                for i in items:
                    temp = randint(0,100)
                    multi = economic_multiplier[economic_level.get()]

                    if (count < 25):
                        if (temp < rarity[i[1]] * multi):
                            q = (rarity[i[1]] / 25) * multi
                            q = randint(0, int(ceil(q)))
                            if (i[2] == 1):
                                attune = "Requires Attunement"
                            if (i[1] == 'L'):
                                q = 1
                            string += (i[0] + ": " + str(q) + " - " + attune + " (From " + i[3] + ')' + "\n")
                            count = count + 1
            else:
                string = '\n' + "===== INVENTORY =====" + '\n' + "Item: Quantity - Price" + '\n' + '\n'
                for i in items:
                    temp = randint(0,100)
                    multi = economic_multiplier[economic_level.get()]

                    if (count < 25):
                        if (temp < rarity[i[1]] * multi):
                            q = (rarity[i[1]] / 10) * multi
                            q = randint(1, int(ceil(q)))
                            if (i[1] == 'L'):
                                q = 1
                            string += (i[0] + ": " + str(q) + " - " + i[2] + "\n")
                            count = count + 1
                    
                
            output.set(string)
            label.config(text = output)
            
        button1 = Button(frame, fg="white smoke", background=lblColor, text="Generate", command=GenInventory) 
        button1.grid(row=2, column=2, padx = 2, pady = 2)
