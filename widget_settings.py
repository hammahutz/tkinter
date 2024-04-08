import tkinter as tk
from tkinter import ttk

def button_func():
    entry_text = entry.get()

    label.config(text=entry_text)
    entry.config(state="disable")

def reset():
    label.config(text="label")
    entry.config(state="enable" )
    entry.set("")

window = tk.Tk()
window.title("Getting and setting widgets")

label = ttk.Label(master=window, text="label")
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text="button", command=button_func)
button.pack()

reset_button = ttk.Button(master=window, text="Reset", command=reset)
reset_button.pack()


window.mainloop()
