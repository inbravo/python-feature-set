# Import tkinter
from tkinter import *
from tkinter import ttk

# Create TK class instance
root = Tk()

# Create a window frame using the TK root
frm = ttk.Frame(root, padding=10)
frm.grid()

# Add a label on the grid
ttk.Label(frm, text="Hello World Arush Cheekooo!").grid(column=0, row=0)

# Add a button on the grid
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

# Run this window in loop (continous)
root.mainloop()