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

        types = readCSV("./CSVs/npcTypes.txt") ## list of NPC types
        pTraits = readCSV("./CSVs/PositiveTraits.txt")
        nTraits = readCSV("./CSVs/NegativeTraits.txt")
        pNums = [0]
        nNums = [0]
        for i in range (len(pTraits)):
            pNums.append(i+1)
        for i in range (len(nTraits)):
            nNums.append(i+1)
        
        Types = StringVar()  ## currently selected NPC type
        Types.set(types[0])

        numP = StringVar() ## Number of positive traits
        numP.set(pNums[0])

        numN = StringVar() ## Number of negative traits
        numN.set(nNums[0])

        opType = OptionMenu(self, Types, *types) ## drop down menu select
        opType.pack()

        optP = OptionMenu(self, numP, *pNums) ## drop down menu select
        optP.pack()

        optN = OptionMenu(self, numN, *nNums) ## drop down menu select
        optN.pack()

        def NPC_Gen(*args):
            output = StringVar()
            PosTrait = StringVar()
            NegTrait = StringVar()
            fetched = ""
            temp = ""
            NPC_Type = ("./CSVs/" + Types.get() + ".txt") ## file path of inventory csv for selected type
            npcs = readCSV(NPC_Type) ## list of npc possibilities
            temp += selectFromList(npcs)
            output.set(temp)
            label = Label(self, textvariable = output) ## output label
            label.pack()
            temp = "Positive Traits: "
            i = 0
            while i < (int(numP.get())):
                fetched = selectFromList(pTraits)
                i += 1
                if (temp.find(fetched) == -1):
                    temp = temp + fetched + ", "
                else:
                    i -= 1
                print (str(i)+"\n")
                print (fetched)
            
            PosTrait.set(temp[0:-2])
            label = Label(self, textvariable = PosTrait) ## output label
            label.pack()
            
            temp = "Negative Traits: "
            for i in range (int(numN.get())):
                fetched = selectFromList(nTraits)
                if (temp.find(fetched) == -1):
                    temp = temp + fetched + ", " 
                    print (temp)
                else:
                    i -= 1
            
            NegTrait.set(temp[0:-2])
            label = Label(self, textvariable = NegTrait) ## output label
            label.pack()
            
            
        button1 = Button(self, text="Generate", command=NPC_Gen) ## button to run process 
        button1.pack()

