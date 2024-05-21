import tkinter as tk
from tkinter import ttk
import calendar 

root = tk.Tk()
screen_w = 250
screen_h = 280
root.geometry(f"{screen_w}x{screen_h}")
root.resizable(False, False)
root.title("Calendar by Vivek")

# Month Label and Options
tk.Label(root, text="Month").grid(row=0, column=0, padx=10, pady=10)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
month_box = ttk.Combobox(root, values=months, width=13, state="readonly")
month_box.grid(row=1, column=0, padx=10)

# Year Label and options
tk.Label(root, text="Year").grid(row=0, column=2, padx=10, pady=10)
years = []
for i  in range(1970, 2051):
    years.append(i)
year_box = ttk.Combobox(root, values=years, width=13, state="readonly")
year_box.grid(row=1, column=2, padx=10)

label = tk.Label(root, font="Arial 11", justify="left")
label.place(x=40,y=120)

def get():
    if year_box.get!="" and month_box.get!='':
        for i in range(1,13):
            if month_box.get() == months[i-1]:
                month = i
        year = int(year_box.get())
        cal = calendar.month(year, month)
        label.config(text=cal)

    else:
        pass

def reset():
    label.config(text="")
    year_box.set("")
    month_box.set("")

get_button = ttk.Button(root, text="Generate", command=get)
get_button.grid(row=2, column=0, padx=10, pady=10)
get_button = ttk.Button(root, text="Reset", command=reset)
get_button.grid(row=2, column=2, padx=10, pady=10)

root.mainloop()