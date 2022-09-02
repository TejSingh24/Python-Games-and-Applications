from cgitb import text
import tkinter as tk
from turtle import xcor

window = tk.Tk()
window.title('Mile To Km Converter')
window.config(width=500, height=400, padx=10, pady=10)

value = tk.Entry(width=10)
value.grid(column=1, row=0, padx=5, pady=5)

label1 = tk.Label(text='Miles')
label1.grid(column=2, row=0, pady=10)
label2 = tk.Label(text='is equal to')
label2.grid(column=0, row=1, pady=10)
label3 = tk.Label(text='Km')
label3.grid(column=2, row=1, pady=10)
label = tk.Label(text='0')
label.grid(column=1, row=1, pady=10)

def convert():
    input = int(value.get()) * 1.609
    label.config(text=input)

calculate = tk.Button(text='Calculate', command=convert)
calculate.grid(column=1, row=2)

window.mainloop()