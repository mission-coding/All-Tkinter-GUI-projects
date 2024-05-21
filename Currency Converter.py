import tkinter as tk
from tkinter import ttk
import requests

root = tk.Tk()
screen_w = 350
screen_h = 85
root.geometry(f"{screen_w}x{screen_h}")
root.resizable(False, False)
root.title("Currency Converter by Vivek")

def get_currencies():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    currencies = list(data["rates"].keys())
    return currencies

def get_exchange_rate():
    url = f"https://api.exchangerate-api.com/v4/latest/{from_combobox.get()}"
    response = requests.get(url)
    data = response.json()
    exchange_rate = data["rates"][to_combobox.get()]
    return exchange_rate

def convert(event=None):
    amount = float(from_entry.get())
    value = amount * get_exchange_rate()
    to_var.set(value)

def interchange():
    from_index = currencies.index(from_combobox.get()) 
    to_index = currencies.index(to_combobox.get()) 
    from_combobox.current(to_index)
    to_combobox.current(from_index)

currencies = get_currencies()
from_combobox = ttk.Combobox(root, values=currencies)
from_combobox.place(x=10, y=2)
from_combobox.current(currencies.index("USD"))  

to_combobox = ttk.Combobox(root, values=currencies)
to_combobox.place(x=screen_w/2+15, y=2)
to_combobox.current(currencies.index("INR"))

from_entry = tk.Entry(root, width=23)
from_entry.place(x=10, y=30)

to_var = tk.StringVar()
to_entry = tk.Entry(root, width=23, state="readonly", textvariable=to_var)
to_entry.place(x=screen_w/2+15, y=30)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.place(x=screen_w/2-30, y=screen_h-30)
from_entry.bind("<Return>", convert)
tk.Button(root, text="⇄", command=interchange).place(x=screen_w/2-15, y=0)
tk.Label(root, text="→", font="Arial 13 bold").place(x=screen_w/2-15, y=28)

root.mainloop()