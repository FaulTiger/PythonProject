import tkinter as tk
import ttkbootstrap as ttk
from widget.Settings import Settings

class Mainmenu:
    
    def __init__(self,window):
        self.window = window
        self.menu()
    
    def menu(self):
        main_frame = ttk.Frame(master = self.window)
        self.settingsimage = ttk.PhotoImage(file = r'C:\repos\PythonProject\assets\cogwheel.png')
        self.image = self.settingsimage.subsample(3, 3)
        settingbutton = ttk.Button(master=main_frame,image=self.image, command = self.settings,style='light-outline')
        settingbutton.pack(expand = 1, side='right')
        main_frame.pack()
        
    def settings(self):
        Settings(self.window)