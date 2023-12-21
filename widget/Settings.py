import ttkbootstrap as ttk

class Settings:
    
    def __init__(self,mainwindow):
        self.mainwindow = mainwindow
        self.window = ttk.Toplevel(parent=None)
        self.window.title('Settings')
        self.window.geometry('1024x600')
        
        mainframe =  ttk.Frame(master=self.window)
        closebutton = ttk.Button(mainframe, text = 'schließen',command=self.closesettings)
        closebutton.pack()
        mainframe.pack()
        
    def closesettings(self):
        self.mainwindow.deiconify()
        self.window.destroy()