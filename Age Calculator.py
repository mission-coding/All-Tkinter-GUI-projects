import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import date

root = tk.Tk()
root.title("Age Calculator")
root.geometry("210x130")
root.resizable(False, False)

var = tk.StringVar()

current_date = str(date.today())
l1 = tk.Label(root, text="")
l2 = tk.Label(root, text="")

tk.Label(root, text="Enter Your Date of Birth").grid(row=0, column=1)

tk.Label(root, text="Year"). grid(row=1, column=0)
dob_year = ttk.Combobox(root, values=[i for i in range(1970, 2025)])
dob_year.grid(row=1, column=1)

tk.Label(root, text="Month"). grid(row=2, column=0)
dob_month = ttk.Combobox(root, values=[i for i in range(1, 13)])
dob_month.grid(row=2, column=1)

tk.Label(root, text="Day"). grid(row=3, column=0)
dob_day = ttk.Combobox(root, values=[i for i in range(1, 32)])
dob_day.grid(row=3, column=1)

def submit(event=None):
    global l1, l2
    l1.destroy()
    l2.destroy()

    current_date_year = int(current_date[0:4])
    current_date_month = int(current_date[5:7])
    current_date_day = int(current_date[8:10])

    dob = var.get()
    print(dob)


    if current_date_day >= int(dob_day.get()):
        day = current_date_day - int(dob_day.get())
    else:
        current_date_month -= 1
        if current_date_month in [1, 3, 5, 7, 8, 10, 12]:
            current_date_day += 31
            day = current_date_day - int(dob_day.get())
        elif current_date_month == 2:
            if current_date_year % 4:
                current_date_day += 29
                day = current_date_day - int(dob_day.get())
            else:
                current_date_day += 28
                day = current_date_day - int(dob_day.get())
        else:
            current_date_day += 30
            day = current_date_day - int(dob_day.get())

    if current_date_month >= int(dob_month.get()):
        month = current_date_month - int(dob_month.get())
    else:
        current_date_year -= 1
        current_date_month += 12
        month = current_date_month - int(dob_month.get())

    year = current_date_year - int(dob_year.get())

    messagebox.showinfo("Your Age", f"You are {year} years, {month} months and {day} days old")

    # l1 = tk.Label(root, text=f"According to Today's Date {current_date}")
    # l2 = tk.Label(root, text=f"You are {year} years, {month} months and {day} days old")
    # l1.grid(row=5, column=1)
    # l2.grid(row=6, column=1)

def reset():
    l1.destroy()
    l2.destroy()
    var.set("")

# f.pack()
b1 = tk.Button(root, text="Submit", command=submit)
b1.grid(row=4, column=1, pady=10)
# b2 = tk.Button(root, text="Reset", command=reset)
# b2.grid(row=5, column=1, pady=10)
root.bind("<Return>", submit)

root.mainloop()
