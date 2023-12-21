import widget.Mainmenu as Mainmenu
import ttkbootstrap as ttk

def init():
    window = ttk.Window(themename='darkly')
    window.title('Auto Mischer')
    window.geometry('1024x600')
    Mainmenu.Mainmenu(window)
    window.mainloop()