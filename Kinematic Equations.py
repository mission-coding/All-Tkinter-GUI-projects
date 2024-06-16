import tkinter as tk
from tkinter import ttk
from math import sqrt

# Create the main window
root = tk.Tk()
screen_w = 670
screen_h = 200
root.geometry(f"{screen_w}x{screen_h}")
root.title("Kinematic Equations Solver")
root.resizable(False, False)

# Title label
tk.Label(text="Choose what you want to find").pack()

# Dropdown to choose the variable to find
variables = ["Acceleration(a)", "Initial Velocity(u)", "Final Velocity(v)", "Time(t)", "Distance(s)"]
to_find = ttk.Combobox(values=variables, state="readonly")
to_find.current(0)
to_find.pack()

tk.Label().pack()
tk.Label(text="Enter Value of all but").pack()
l1 = tk.Label()
l1.pack()

# Create frames for input fields
f1 = tk.Frame()
f1.pack(side="left", padx=10)
f2 = tk.Frame()
f2.pack(side="left", padx=10)
f3 = tk.Frame()
f3.pack(side="left", padx=10)
f4 = tk.Frame()
f4.pack(side="left", padx=10)

# Labels and entries for the input fields
var1 = tk.Label(f1)
var1.pack()
var1_entry = ttk.Entry(f1)
var1_entry.pack()

var2 = tk.Label(f2)
var2.pack()
var2_entry = ttk.Entry(f2)
var2_entry.pack()

var3 = tk.Label(f3)
var3.pack()
var3_entry = ttk.Entry(f3)
var3_entry.pack()

var4 = tk.Label(f4)
var4.pack()
var4_entry = ttk.Entry(f4)
var4_entry.pack()

f5 = tk.Frame()
f5.pack()

# Label to display the answer
ans_label = tk.Label()
ans_label.pack()

# Function to update the UI based on the selected variable to find
def update_ui(event=None):
    if to_find.get() == "Acceleration(a)":
        l1.config(text="Please enter value of 'any one' Time(t) or Distance(s)")
        var1.config(text="Final Velocity(v)")
        var2.config(text="Initial Velocity(u)")
        var3.config(text="Time(t)")
        var4.config(text="Distance(s)")

    if to_find.get() == "Final Velocity(v)":
        l1.config(text="Please enter value of 'any one' Time(t) or Distance(s)")
        var1.config(text="Acceleration(a)")
        var2.config(text="Initial Velocity(u)")
        var3.config(text="Time(t)")
        var4.config(text="Distance(s)")

    if to_find.get() == "Distance(s)":
        l1.config(text="Please enter value of 'any one' from Time(t) or Final Velocity(v)")
        var1.config(text="Acceleration(a)")
        var2.config(text="Initial Velocity(u)")
        var3.config(text="Time(t)")
        var4.config(text="Final Velocity(v)")

    if to_find.get() == "Initial Velocity(u)":
        l1.config(text="Please enter value of 'any two' from Time(t), Final Velocity(v) or Initial Velocity(u)")
        var1.config(text="Acceleration(a)")
        var2.config(text="Final Velcocity(v)")
        var3.config(text="Time(t)")
        var4.config(text="Distance(s)")

    if to_find.get() == "Time(t)":
        l1.config(text="Please enter value of 'any one' from Final Velocity(v) or Distance(s)")
        var1.config(text="Acceleration(a)")
        var2.config(text="Initial Velocity(u)")
        var3.config(text="Final Velocity(v)")
        var4.config(text="Distance(s)")

# Function to calculate and display the result
def done():
    if to_find.get() == "Acceleration(a)":
        v = var1_entry.get()
        u = var2_entry.get()
        t = var3_entry.get()
        s = var4_entry.get()

        try:
            # Using the formula a = (v - u) / t
            a = (float(v) - float(u)) / float(t)
            a = round(a, 3)
            ans_label.config(text="a = " + str(a), fg="Green")
        except:
            try:
                # Using the formula a = (v^2 - u^2) / (2s)
                a = (float(v)**2 - float(u)**2) / (2 * float(s))
                a = round(a, 3)
                ans_label.config(text="a = " + str(a), fg="Green")
            except:
                ans_label.config(text="Invalid Input !", fg="Red")

    if to_find.get() == "Final Velocity(v)":
        a = var1_entry.get()
        u = var2_entry.get()
        t = var3_entry.get()
        s = var4_entry.get()

        try:
            # Using the formula v = u + at
            v = float(u) + float(a) * float(t)
            v = round(v, 3)
            ans_label.config(text="v = " + str(v), fg="Green")
        except:
            try:
                # Using the formula v^2 = u^2 + 2as
                v = sqrt(2 * float(a) * float(s) + float(u)**2)
                v = round(v, 3)
                ans_label.config(text="v = " + str(v), fg="Green")
            except:
                ans_label.config(text="Invalid Input !", fg="Red")

    if to_find.get() == "Distance(s)":
        a = var1_entry.get()
        u = var2_entry.get()
        t = var3_entry.get()
        v = var4_entry.get()

        try:
            # Using the formula s = ut + 0.5at^2
            s = float(u) * float(t) + 0.5 * float(a) * float(t)**2
            s = round(s, 3)
            ans_label.config(text="s = " + str(s), fg="Green")
        except:
            try:
                # Using the formula s = (v^2 - u^2) / 2a
                s = (float(v)**2 - float(u)**2) / (2 * float(a))
                s = round(s, 3)
                ans_label.config(text="s = " + str(s), fg="Green")
            except:
                ans_label.config(text="Invalid Input !", fg="Red")

    if to_find.get() == "Initial Velocity(u)":
        a = var1_entry.get()
        v = var2_entry.get()
        t = var3_entry.get()
        s = var4_entry.get()

        try:
            # Using the formula u = v - at
            u = float(v) - float(a) * float(t)
            u = round(u, 3)
            ans_label.config(text="u = " + str(u), fg="Green")
        except:
            try:
                # Using the formula u = (s - 0.5at^2) / t
                u = (float(s) - 0.5 * float(a) * float(t)**2) / float(t)
                u = round(u, 3)
                ans_label.config(text="u = " + str(u), fg="Green")
            except:
                try:
                    # Using the formula u = sqrt(v^2 - 2as)
                    u = sqrt(float(v)**2 - 2 * float(a) * float(s))
                    u = round(u, 3)
                    ans_label.config(text="u = " + str(u), fg="Green")
                except:
                    ans_label.config(text="Invalid Input !", fg="Red")

    if to_find.get() == "Time(t)":
        a = var1_entry.get()
        u = var2_entry.get()
        v = var3_entry.get()
        s = var4_entry.get()

        try:
            # Using the formula t = (v - u) / a
            t = (float(v) - float(u)) / float(a)
            t = round(t, 3)
            ans_label.config(text="t = " + str(t), fg="Green")
        except:
            try:
                # Solving the quadratic equation 0.5at^2 + ut - s = 0
                a1 = float(a) / 2
                b = float(u)
                c = -float(s)

                D = b**2 - 4 * a1 * c

                if D >= 0:
                    sol1 = (-b + sqrt(D)) / (2 * a1)
                    sol1 = round(sol1, 3)
                    sol2 = (-b - sqrt(D)) / (2 * a1)
                    sol2 = round(sol2, 3)

                if sol1 >= 0:
                    ans_label.config(text="t = " + str(sol1), fg="Green")
                elif sol2 >= 0:
                    ans_label.config(text="t = " + str(sol2), fg="Green")
                else:
                    print(sol1, sol2)

            except:
                ans_label.config(text="Invalid Input !", fg="Red")

# Button to calculate the result
tk.Button(f5, text="Done", command=done).pack()

# Bind the combobox selection event to update the UI
to_find.bind("<<ComboboxSelected>>", update_ui)
update_ui()

# Run the main event loop
root.mainloop()
