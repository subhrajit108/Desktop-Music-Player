#import modules
import cv2
import pygame
import tkinter as tkr
import os
from tkinter.filedialog  import askdirectory
from tkinter.ttk import *
from PIL import ImageTk,Image
#create window

player=tkr.Tk()
songlist=[]
pth='C:/Users/Subhrajit/Downloads/itachi.ico'
player.iconbitmap(pth)
lbl=tkr.Label(player, text = 'Music is the bridge to the soul', font =('Chicle', 15)).pack(side = "top", pady = 10)
#creating canvas
cv_img = cv2.cvtColor(cv2.imread(r"C:\Users\Subhrajit\Downloads\rsz_doodlemusic.jpg"), cv2.COLOR_BGR2RGB)
height, width, no_channels = cv_img.shape
canvas = tkr.Canvas(player, width = 200, height = 200)
canvas.pack()
# Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
photo = ImageTk.PhotoImage(image = Image.fromarray(cv_img))
canvas.create_image(0, 0, image=photo, anchor=tkr.NW)

#edit window

player.title("Audio Player")
player.geometry("500x500")

#playlist register
os.chdir('C:/Users/Subhrajit/Music')

def directorychooser():
    directory = askdirectory()
    os.chdir(directory)
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            songlist.append(files)
            print(files)


    pygame.mixer.init()
    songlist.reverse()

directorychooser()

#playlist input
playlist=tkr.Listbox(player,highlightcolor="blue",selectmode=tkr.SINGLE)
print(songlist)
for item in songlist:
    pos=0
    playlist.insert(pos,item)
    pos=pos+1


#initialization
pygame.init()
pygame.mixer.init()
#action event
def Play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()



def ExitPlayer():
    pygame.mixer.music.stop()

def Pause():
    pygame.mixer.music.pause()

def UnPause():
    pygame.mixer.music.unpause()

def VolumeControl(val):
    volume=int(val)/100

    pygame.mixer.music.set_volume(volume)
    #print(pygame.mixer.music.get_volume())
    #print(VolumeLevel.get())

#volume control
VolumeLevel=tkr.Scale(player,from_=0, to_=100,orient=tkr.HORIZONTAL,command=VolumeControl)
#register buttons

button1=tkr.Button(player,width=5,height=3,text="PLAY",command=Play)
button2=tkr.Button(player,width=5,height=3,text="STOP",command=ExitPlayer)
button3=tkr.Button(player,width=5,height=3,text="PAUSE",command=Pause)
button4=tkr.Button(player,width=5,height=3,text="RESUME",command=UnPause)


#song name

var=tkr.StringVar()
songtitle=tkr.Label(player,textvariable=var)


#place widgets
songtitle.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
VolumeLevel.pack()
playlist.pack(fill="both",expand="yes")
player.config(bg='#00ffcc')
#activate

player.mainloop()

