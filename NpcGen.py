## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere


from KeepFunctions import *


class NpcGen(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("NPC Generator") 
        self.geometry("400x400")

        # set label font
        lblFont = tkFont.Font(family='Helvetica', size=24, weight=tkFont.BOLD)
        btnFont = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)

        # sets background color
        self.configure(background=BgColor)

        types = readCSV("./CSVs/npcTypes.txt") ## list of NPC types
        pTraits = readCSV("./CSVs/PositiveTraits.txt")
        nTraits = readCSV("./CSVs/NegativeTraits.txt")
        pNums = [0]
        nNums = [0]
        for i in range (0,5):
            pNums.append(i+1)
        for i in range (0,5):
            nNums.append(i+1)
        
        Types = StringVar()  ## currently selected NPC type
        Types.set(types[0])

        numP = StringVar() ## Number of positive traits
        numP.set(pNums[0])

        numN = StringVar() ## Number of negative traits
        numN.set(nNums[0])

        labelType = Label(self, fg="white smoke", background=BgColor, text = "NPC Type")
        labelType.pack()
        opType = OptionMenu(self, Types, *types) ## drop down menu select
        opType.config(fg="white smoke", background=lblColor)
        opType.pack()

        labelType = Label(self, fg="white smoke", background=BgColor, text = "Positive traits")
        labelType.pack()
        optP = OptionMenu(self, numP, *pNums) ## drop down menu select
        optP.config(fg="white smoke", background=lblColor)
        optP.pack()

        labelN = Label(self, fg="white smoke", background=BgColor, text = "Negative traits")
        labelN.pack()
        optN = OptionMenu(self, numN, *nNums) ## drop down menu select
        optN.config(fg="white smoke", background=lblColor)
        optN.pack()

        labelOutputType = Label(self, fg="white smoke", background=BgColor, text = "")
        labelOutputType.pack()
        labelOutputP = Label(self, fg="white smoke", background=BgColor, text = "")
        labelOutputP.pack()
        labelOutputN = Label(self, fg="white smoke", background=BgColor, text = "")
        labelOutputN.pack()

        def NPC_Gen(*args):
            output = StringVar()
            PosTrait = StringVar()
            NegTrait = StringVar()
            fetched = ""
            temp = ""
            NPC_Type = ("./CSVs/NPCs/" + Types.get() + ".txt") ## file path of inventory csv for selected type
            npcs = readCSV(NPC_Type) ## list of npc possibilities
            temp += selectFromList(npcs)
            output.set(temp)
            labelOutputType.config(text = output.get())
            temp = "Positive Traits: "
            i = 0
            while i < (int(numP.get())):
                fetched = selectFromList(pTraits)
                i += 1
                if (temp.find(fetched) == -1):
                    temp = temp + fetched + ", "
                else:
                    i -= 1
                
            
            PosTrait.set(temp[0:-2])
            labelOutputP.config(text = PosTrait.get())
            
            temp = "Negative Traits: "
            for i in range (int(numN.get())):
                fetched = selectFromList(nTraits)
                if (temp.find(fetched) == -1):
                    temp = temp + fetched + ", " 
                    
                else:
                    i -= 1
            
            NegTrait.set(temp[0:-2])
            labelOutputN.config(text = NegTrait.get())


        def Clear():
            labelOutputType.config(text = "")
            labelOutputP.config(text = "")
            labelOutputN.config(text = "")
            
            
        button1 = Button(self, fg="white smoke", background=lblColor, text="Generate", command=NPC_Gen) ## button to run process 
        button1.pack()

