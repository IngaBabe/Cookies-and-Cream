from Internals import Connection
from tkinter import *
import socket
import threading

class Window(Frame):
    def __init__(self, master = None)
        Frame.__init__(self, master)
        self.master = master
        self.LoadUI()
    
    def LoadUI(self):
        self.MenuBar = Menu(self)
        self.Connect = Menu(self.MenuBar, tearoff = 0)
        self.Connect.add_command(label = "Lan", menu = self.Lan_UI)
        
        self.MenuBar.add_cascade(label = "Connect", menu = self.Connect)
        
        self.master.title("Cookies & Cream")
        self.master.config(menu = self.MenuBar)
        width,height=self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0" % (width, height))
        self.pack(fill=BOTH, expand=1)
        
        self.LanUI = Label(self) # Lan GUI
        self.LanUI.pack(fill = BOTH, expand = 1)
        
        self.Lan_Servers = Frame(self.LanUI)
        self.LanUI.pack(fill = BOTH, expand = 1)
        
        self.Lan_Status = Text(self.LanUI)
        self.Lan_Status.pack(fill=BOTH, expand=1)
        self.Lan_Status.insert("end", "Status")
        self.Lan_Status.config(state=DISABLED)
        
        self.LanUI.pack_forget()
        
        self.ChatUI=Label(self) # CHATGUI
        self.ChatUI.pack(fill=BOTH, expand=1)

        self.ChatFrame=Frame(self.ChatUI, height=10)
        self.ChatFrame.pack(fill=BOTH, expand=1)

        self.ChatLog=Text(self.ChatUI)
        self.ChatLog.pack(fill=BOTH, expand=1)
        self.ChatLog.config(state=DISABLED)

        self.ChatUI.pack_forget()
        
    def Lan_UI(self):
        self.LanUI.pack(fill=BOTH, expand=1)
        self.UpdateStatus(self.Lan_Status, "Searching for servers on LAN...")
        
        PortScanner = Connection.PortScan()
        Ports = PortScanner.Start()
