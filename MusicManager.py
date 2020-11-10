## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere

from KeepFunctions import *

class MusicManage(Toplevel): 
      
    def __init__(self, master = None): 
          
        super().__init__(master = master) 
        self.title("New Window") 
        self.geometry("200x200")

        track = filedialog.askopenfilename(initialdir = "./Music", title = "Select a File", filetypes = (("MP3", "*.mp3*"), ("all files",  "*.*")))
        
        label = Label(self, text ="This is a new Window")
        label.pack(fill = X, padx=5, pady=5)
