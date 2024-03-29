## The Keep TTRPG Toolbox
## VTC Senior Project 20/21
## Adam Bourque
## Zachary Hess
## Austin Lalumiere


from KeepFunctions import *
from pygame import mixer

num = 0
tracks = []
volumes = []

class MusicManage(Toplevel): 
    def __init__(self, master = None):

        super().__init__(master = master)

        self.title("Music Manager")
        self.geometry("600x400")
        self.iconbitmap(r"The-Keep.ico")
        
        mixer.init()

        # set lable font
        lblFont = tkFont.Font(family='Helvetica', size=24, weight=tkFont.BOLD)
        btnFont = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)

        vol_label = Label(self, fg="white smoke", background=BgColor, text = "Volume")

        # sets bacckground color
        self.configure(background=BgColor)

        def PlayTrack(track, chan):
            global tracks
            global volumes
            mixer.Channel(chan).set_volume(volumes[chan])
            mixer.Channel(chan).play(mixer.Sound(track), -1)

        def PauseTrack(track, chan):
            mixer.Channel(chan).pause()

        def UnPauseTrack(track, chan):
            mixer.Channel(chan).unpause()

        def StopTrack(track, chan):
            mixer.Channel(chan).stop()

        def change_vol(_=None):
            global num
            global volumes
            i = num - 1                        # changes when new track added = bad, no good solution.
            volumes[i] = volSlide.get()
            mixer.Channel(i).set_volume(volumes[i])
            
        def NewTrack():
            global num
            global tracks
            global volumes
            
            i = num
            volumes.append(0.5)
            vol_label.grid(row=0, column=5, padx = 2, pady = 2)
                
            track = filedialog.askopenfilename(initialdir = "./Music", title = "Select a File", filetypes = (("MP3", "*.mp3*"), ("all files",  "*.*")))
            if (str(track) != ''):
                tracks.append(track)
                
                temp = track.split("/")
                label = Label(self, fg="white smoke", background=BgColor, text = temp[-1])
                label.grid(row=num+1, column=0, padx = 2, pady = 2)

                btnPlay = Button(self, fg="white smoke", background=lblColor, text ="Play")
                btnPlay.bind("<Button>", lambda e: PlayTrack(tracks[i], i))
                btnPlay.grid(row=i+1, column=1, padx = 2, pady = 2)

                btnPause = Button(self, fg="white smoke", background=lblColor, text ="Pause")
                btnPause.bind("<Button>", lambda e: PauseTrack(tracks[i], i))
                btnPause.grid(row=i+1, column=2, padx = 2, pady = 2)

                btnUnPause = Button(self, fg="white smoke", background=lblColor, text ="Resume")
                btnUnPause.bind("<Button>", lambda e: UnPauseTrack(tracks[i], i))
                btnUnPause.grid(row=i+1, column=3, padx = 2, pady = 2)

                btnStop = Button(self, fg="white smoke", background=lblColor, text ="Stop")
                btnStop.bind("<Button>", lambda e: StopTrack(tracks[i], i))
                btnStop.grid(row=i+1, column=4, padx = 2, pady = 2)
                
                volSlide.set(0.5)
                volSlide.grid(row=i+1, column=5, padx = 2, pady = 2)
                
                num += 1
            else:
                file_error()

        volSlide = Scale(self, orient = HORIZONTAL, from_=0, to=1, resolution=0.02, command = change_vol, fg="white smoke", background=lblColor, highlightbackground = BgColor, highlightcolor = BgColor)

        btnAdd = Button(self, text ="Add Track",fg="white smoke", background=lblColor)
        btnAdd.bind("<Button>", lambda e: NewTrack())
        btnAdd.grid(row=0, column=0, padx = 2, pady = 2)

        


            
