import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pygame
from tkinter import ttk
from ttkthemes import themed_tk as tk
import webbrowser

#Make songs that are double-clicked, played
def selected_song(*args):
	selected = listbox.curselection()
	pygame.mixer.music.play(1)
	updatelabel()

def closeapp(*args):
	root.destroy()

def opengithub():
	webbrowser.open_new("https://github.com/sketchyboi14")

def aboutpymusicplayer(*args):
	messagebox.showinfo("About PyMusic Player", "PyMusic Player was built by sketchyboi14 in python. Go to https://github.com/sketchyboi14/PyMusicPlayer/issues to report issues.")

def nextsong(*args):
	global index
	index += 1
	pygame.mixer.music.load(listofsongs[index])
	pygame.mixer.music.play()
	updatelabel()

def prevsong(*args):
	global index
	index -= 1
	pygame.mixer.music.load(listofsongs[index])
	pygame.mixer.music.play()
	updatelabel()

def stopsong(*args):
	pygame.mixer.music.stop()
	v.set("")

def updatelabel():
	global index
	v.set(listofsongs[index])

def directorychooser(*args):
	directory = filedialog.askdirectory(title="Select Folder")
	os.chdir(directory)

	for files in os.listdir(directory):
		if files.endswith(".mp3"):
			listofsongs.append(files)

	for files in os.listdir(directory):
		if files.endswith(".wav"):
			listofsongs.append(files)

	for files in os.listdir(directory):
		if files.endswith(".ogg"):
			listofsongs.append(files)

	for files in os.listdir(directory):
		if files.endswith(".flac"):
			listofsongs.append(files)

	pygame.mixer.init()
	pygame.mixer.music.load(listofsongs[0])

root = tk.ThemedTk()
root.get_themes()
root.set_theme("breeze")
root.minsize(300,300)
root.title("PyMusic Player")
appicon = PhotoImage(file="icons/purphalfnote.png")
root.tk.call("wm", "iconphoto", root._w, appicon)

nextbtnicon = PhotoImage(file="icons/playbutton.png")
prevbtnicon = PhotoImage(file="icons/prevbutton.png")
stopbtnicon = PhotoImage(file="icons/stop.png")
githubbtnicon = PhotoImage(file="icons/githublogo.png")
openfoldericon = PhotoImage(file="icons/openicon.png")
closeicon = PhotoImage(file="icons/closeicon.png")
infoicon = PhotoImage(file="icons/infoicon.png")

v = StringVar()
songlabel = Label(root, textvariable=v, width=35)

listofsongs = []
index = 0

root.iconify()
messagebox.showinfo("Attention!", "Welcome to PyMusic Player. After you click OK, the file manager will open. Navigate to a folder that contains audio files such as mp3 or wav.")
root.deiconify()
directorychooser()

label = Label(root, text="Songs", font=("Meera", 10, "bold"), fg="blue")
label.pack()

listbox = Listbox(root, width=50)
listbox.pack()

reversedlist = listofsongs.reverse()

for items in listofsongs:
	listbox.insert(0,items)

nextbutton = ttk.Button(root, command=nextsong, image=nextbtnicon)
nextbutton.pack(side=RIGHT)
root.bind("<Right>", nextsong)

previousbutton = ttk.Button(root, command=prevsong, image=prevbtnicon)
previousbutton.pack(side=LEFT)
root.bind("<Left>", prevsong)

stopbutton = ttk.Button(root, command=stopsong, image=stopbtnicon)
stopbutton.pack()
root.bind("<space>", stopsong)

songlabel.pack()

githubbtn = Button(root, image=githubbtnicon, command=opengithub, relief="flat")
githubbtn.pack()

menu = Menu(root)
submenu = Menu(menu, tearoff=False)

menu.add_cascade(label="File", menu=submenu, font=("Meera", 10, "bold"))
submenu.add_command(label="Open Folder", command=directorychooser, font=("Meera", 10, "bold"), accelerator="Ctrl O", compound=LEFT, image=openfoldericon)
submenu.add_command(label="Close", command=root.destroy, font=("Meera", 10, "bold"), accelerator="Ctrl W", compound=LEFT, image=closeicon)


submenu = Menu(menu, tearoff=False)

menu.add_cascade(label="Help", menu=submenu, font=("Meera", 10, "bold"))
submenu.add_command(label="About PyMusic Player", command=aboutpymusicplayer, font=("Meera", 10, "bold"), accelerator="Ctrl H", compound=LEFT, image=infoicon)

root.bind("<Control-o>", directorychooser)
root.bind("<Control-w>", closeapp)
root.bind("<Control-h>", aboutpymusicplayer)
listbox.bind("<Double-Button-1>", selected_song)

root.config(menu=menu)

root.mainloop()
