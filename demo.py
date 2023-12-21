import tkinter as tk
#import tkinter as ttk
import ttkbootstrap as ttk

def convert():
    mile_Input = entry_int.get()
    km_Output = mile_Input * 1.61
    outpt_String.set(km_Output)
    
Helloworld = 'Hello'

#window
window = ttk.Window(themename='darkly')
window.title('Demo')

window.geometry('300x150')

#titel
label = ttk.Label(master = window,text = Helloworld,font = 'Calibri 13 bold')
label.pack()

#input
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
ttk.Entry(master = input_frame,textvariable=entry_int).pack(side='left')
button = ttk.Button(master = input_frame, text = 'Convert',command= convert)
#entry.pack(side = 'left')
button.pack(side = 'left')
input_frame.pack(pady = 10)

#output
outpt_String = tk.StringVar()
output_label = ttk.Label(master=window,
                         text='Output',
                         font='Calibri 24',
                         textvariable=outpt_String)
output_label.pack(pady=5)

#sidemenu


#run
window.mainloop()
