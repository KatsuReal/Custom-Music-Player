import tkinter as tk
import tkinter.font as tkFont
import pygame
from tkinter import *
from tkinter import filedialog

window = tk.Tk()
window.title("Custom Music Player")
window.geometry("300x350")

pygame.mixer.init()
window.configure(background="slategray")

songs = Listbox(window, bg = "black", fg = "white", width = 60, selectbackground = "gray", selectforeground = "black")
songs.pack(pady = 20)

menu = Menu(window)
window.config(menu = menu)

def add_song():
   song = filedialog.askopenfilename(initialdir = 'music/', title = "Choose a song", filetypes =(("mp3 Files", "*.mp3"), ))
   songs.insert(END, song)

addsong = Menu(menu)
menu.add_cascade(label = "Add a song", menu = addsong)
addsong.add_command(label = "Add a song", command = add_song)

def play():
   song = songs.get(ACTIVE)

   pygame.mixer.music.load(song)
   pygame.mixer.music.play(loops = 0)

def stop():
   pygame.mixer.music.stop()
   songs.selection_clear(ACTIVE)

btn1 = tk.Button(window, text ="Play", command=play, bg="black", fg="white")
btn1.pack(pady=20, padx=10)

btn2 = tk.Button(window, text ="Stop", command=stop, bg="black", fg="white")
btn2.pack(pady=20, padx=10)

window.mainloop()
