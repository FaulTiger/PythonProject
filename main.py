import tkinter as tk
import tkinter as ttk

Helloworld = 'Hello'
print(Helloworld)

#window
window = tk.Tk()
window.title('Demo')
window.geometry('300x150')

#titel
label = ttk.Label(master = window,text = Helloworld,font = 'Calibri 13 bold')
label.pack()

#input
input_frame = ttk.Frame(master = window)
entry = ttk.Entry(master = input_frame)
button = ttk.Button(master = input_frame, text = 'Convert')
entry.pack(side = 'left')
button.pack(side = 'left')
input_frame.pack(pady = 10)

#run
window.mainloop()
