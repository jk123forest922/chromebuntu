import pygame
import win32api
from win32api import GetSystemMetrics
import win32con
import win32gui
import time
import os
import tkinter as tk
import random

TRANS_COLOR = "white"

DOT_x = 683
DOT_y = 338

dot_size = 100

print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))

root = tk.Tk()
root.overrideredirect(True) # borderless window
root.geometry("+683+334") # top-right corner
root.attributes("-transparentcolor", TRANS_COLOR) # set transparent color
root.attributes("-topmost", 1) # make it on top of other windows

canvas = tk.Canvas(root, width=GetSystemMetrics(0), height=GetSystemMetrics(1), bg=TRANS_COLOR, highlightthickness=0)
canvas.pack()

dot = canvas.create_oval(0, 0, dot_size, dot_size, outline='')

def blinking_dot(i=0):
    global DOT_x, DOT_y
    colors = (TRANS_COLOR, "red")
    canvas.itemconfigure(dot, fill=colors[i])
    root.after(250, blinking_dot, 1-i)
    root.geometry("+{}+{}".format(int(DOT_x - (dot_size/2)), int(DOT_y - (dot_size/2))))
    DOT_x -= 10
    DOT_y -= 10
blinking_dot() # start blinking dot
root.mainloop()