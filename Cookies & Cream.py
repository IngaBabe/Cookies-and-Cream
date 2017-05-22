from Internals import Connection
from tkinter import *
import socket

class Window(Frame):
    def __init__(self, master = None)
        Frame.__init__(self, master)
        self.master = master
        self.LoadUI()
    
    def LoadUI(self):
        self.MenuBar = Menu(self)
        self.Connect = Menu(self.MenuBar, tearoff = 0)
        
        self.MenuBar.add_cascade(label = "Lan", menu = self.Connect)
