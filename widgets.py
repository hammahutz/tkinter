import tkinter as tk
from tkinter import ttk


def button_func():
    print("Button is pressed")


# create a window
window = tk.Tk()
window.title("Windows and widgets")
window.geometry("800x500")

# ttk label
label = ttk.Label(master=window, text="This is a test")
label.pack()

# tk text
text = tk.Text(master=window)
text.pack()

# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# ttk button
button = ttk.Button(master=window, text="A button", command=button_func)
button.pack()


ex_button = ttk.Button(
    master=window, text="A button", command=lambda: print("hello world")
)
ex_button.pack()

# run
window.mainloop()
