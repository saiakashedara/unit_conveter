import tkinter as tk
from logic import *

def convert_temp():
    c = float(entry1.get())
    result.set(round(celsius_to_fahrenheit(c), 2))


def convert_distance():
    km = float(entry1.get())
    result.set(round(km_to_miles(km), 2))


def convert_weight():
    kg = float(entry1.get())
    result.set(round(kg_to_pounds(kg), 2))


root = tk.Tk()
root.title("Unit Converter")

entry1 = tk.Entry(root)
entry1.pack()

result = tk.StringVar()

tk.Button(root, text="Celsius → Fahrenheit", command=convert_temp).pack()
tk.Button(root, text="Km → Miles", command=convert_distance).pack()
tk.Button(root, text="Kg → Pounds", command=convert_weight).pack()

tk.Label(root, textvariable=result).pack()

root.mainloop()