from tkinter import *
from tkinter import ttk

root = Tk() #Este es el marco principal de la aplicacion
frame = ttk.Frame(root, padding = 10)
frame.grid()
label = Label(frame, text="HOLA TKINTER", padx=0, pady=20, fg="blue", bg="green")
label.grid(row=0, column=0)
label2 = Label(frame, text="ADIOS TKINTER!!!!!!", bg="#000000", fg="white")
label2.grid(row=1, column=1)
root.mainloop()
