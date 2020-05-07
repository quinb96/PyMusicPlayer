import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pygame
from tkinter import ttk
from ttkthemes import themed_tk as tk
import webbrowser

def opengithub():
	webbrowser.open_new("https://github.com/sketchyboi14")

def aboutmp():
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
	return songname

def updatelabel():
	global index
	global songname
	v.set(listofsongs[index])
	return songname

def directorychooser():
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
appicon = PhotoImage(file="purphalfnote.png")
root.tk.call("wm", "iconphoto", root._w, appicon)

nextbtnicon = PhotoImage(file="playbutton.png")
prevbtnicon = PhotoImage(file="prevbutton.png")
stopbtnicon = PhotoImage(file="stop.png")
githubbtnicon = PhotoImage(file="githublogo.png")

v = StringVar()
songlabel = Label(root, textvariable=v, width=35)

listofsongs = []
index = 0

messagebox.showinfo("Attention!", "Welcome to PyMusic Player. After you click OK, the file manager will open. Navigate to a folder that contains audio files such as mp3 or wav.")
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
nextbutton.bind("<Right>", nextsong)

previousbutton = ttk.Button(root, command=prevsong, image=prevbtnicon)
previousbutton.pack(side=LEFT)
previousbutton.bind("<Left>", prevsong)

stopbutton = ttk.Button(root, command=stopsong, image=stopbtnicon)
stopbutton.pack()
stopbutton.bind("<space>", stopsong)

songlabel.pack()

githubbtn = Button(root, image=githubbtnicon, command=opengithub)
githubbtn.pack()

menu = Menu(root)
submenu = Menu(menu)

menu.add_cascade(label="File", menu=submenu, font=("Meera", 10, "bold"))
submenu.add_command(label="Open Folder", command=directorychooser, font=("Meera", 10, "bold"))
submenu.add_command(label="Close", command=root.destroy, font=("Meera", 10, "bold"))
root.config(menu=menu)

submenu = Menu(menu)

menu.add_cascade(label="Help", menu=submenu, font=("Meera", 10, "bold"))
submenu.add_command(label="About PyMusic Player", command=aboutmp, font=("Meera", 10, "bold"))

root.mainloop()