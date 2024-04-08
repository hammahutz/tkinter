import tkinter as tk
from tkinter import ttk

def btn():
    

window = tk.Tk()
window.title("Tkinter variables")

# tkinter variable
string_var = tk.StringVar(value="Start value")


label = ttk.Label(master=window, text="label", textvariable=string_var)
label = label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry = entry.pack()

button = ttk.Button(master=window, text = "button", command=btn)

window.mainloop()
