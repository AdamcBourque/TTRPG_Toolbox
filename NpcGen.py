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

        frame = Frame(self)
        frame.config(bg = BgColor)
        frame.pack()

        lblfrme = Frame(self)
        lblfrme.config(bg = BgColor)
        lblfrme.pack()

        labelType = Label(frame, fg="white smoke", background=BgColor, text = "NPC Type")
        labelType.grid(row=0, column=0, padx = 2, pady = 2)
        opType = OptionMenu(frame, Types, *types) ## drop down menu select
        opType.config(fg="white smoke", background=lblColor)
        opType.grid(row=1, column=0, padx = 2, pady = 2)

        labelType = Label(frame, fg="white smoke", background=BgColor, text = "Positive traits")
        labelType.grid(row=0, column=1, padx = 2, pady = 2)
        optP = OptionMenu(frame, numP, *pNums) ## drop down menu select
        optP.config(fg="white smoke", background=lblColor)
        optP.grid(row=1, column=1, padx = 2, pady = 2)

        labelN = Label(frame, fg="white smoke", background=BgColor, text = "Negative traits")
        labelN.grid(row=0, column=2, padx = 2, pady = 2)
        optN = OptionMenu(frame, numN, *nNums) ## drop down menu select
        optN.config(fg="white smoke", background=lblColor)
        optN.grid(row=1, column=2, padx = 2, pady = 2)

        labelOutputType = Label(lblfrme, fg="white smoke", background=BgColor, text = "")
        labelOutputType.grid(row=1, column=0, padx = 2, pady = 2)
        labelOutputP = Label(lblfrme, fg="white smoke", background=BgColor, text = "")
        labelOutputP.grid(row=2, column=0, padx = 2, pady = 2)
        labelOutputN = Label(lblfrme, fg="white smoke", background=BgColor, text = "")
        labelOutputN.grid(row=3, column=0, padx = 2, pady = 2)

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
            
            
        button1 = Button(frame, fg="white smoke", background=lblColor, text="Generate", command=NPC_Gen) ## button to run process 
        button1.grid(row=1, column=3, padx = 2, pady = 2)

