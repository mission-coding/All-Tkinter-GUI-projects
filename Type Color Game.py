import tkinter as tk
import random 

# Create the main window
root = tk.Tk()
screen_w = 250
screen_h = 200
root.geometry(f"{screen_w}x{screen_h}")
root.resizable(False, False)
root.title("Type Color Game by Vivek")

# Global variables
score = 0
time_left = 30

# Labels to display score and time left
tk.Label(root, text="Type Word's Color not Word", font="Helvetica 12").pack(pady=10)
score_label = tk.Label(root, text=f"Score: {score}", font="Helvetica 10")
score_label.pack()
time_left_label = tk.Label(root, text=f"Time Left: {time_left}", font="Helvetica 10") 
time_left_label.pack()

# Lists of color names and colors
names = ["Red", "Black", "White", "Pink", "Orange", "Purple", "Blue", "Green", "Yellow"]
colors = ["Red", "Black", "Pink", "Orange", "Purple", "Blue", "Green", "Yellow"]

# Get random color name and color
random_name = names[random.randint(0, len(names)-1)].lower()
random_color = colors[random.randint(0, len(colors)-1)].lower()

# Label to display the random color name
name_label = tk.Label(root, font="Helvetica 25", text=random_name, fg=random_color)
name_label.pack()

# Entry widget for user input
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font="Helvetica 12", width=15)
entry.pack()

# Function to countdown the time
def countdown(event=None):
    global time_left
    if time_left > 0:
        time_left = time_left -1
        time_left_label.config(text=f"Time Left: {time_left}")
        root.after(1000, countdown, time_left)
    else:
        time_left_label.config(text="Time's Up", fg="red")
        entry_var.set("")
        entry.config(state="readonly")

# Function to check user input
def check(event=None):
    global random_name, random_color, score
    if entry_var.get() == name_label.cget('fg') and time_left>0:
        random_name = names[random.randint(0, len(names)-1)].lower()
        random_color = colors[random.randint(0, len(colors)-1)].lower()
        name_label.config(text=random_name, fg=random_color)
        score += 1
        score_label.config(text=f"Score: {score}")
        entry_var.set("")

# Bind events to functions
entry.bind("<Button-1>", countdown)
if time_left>0:
    entry.bind("<Return>", check)

# Function to reset the game
def reset():
    root.focus_force()
    global time_left, score, random_name, random_color
    time_left = 30
    time_left_label.config(text=f"Time Left: {time_left}", fg="Black")
    score = 0
    score_label.config(text=f"Score: {score}")
    random_name = names[random.randint(0, len(names)-1)].lower()
    random_color = colors[random.randint(0, len(colors)-1)].lower()
    name_label.config(text=random_name, fg=random_color)
    entry.config(takefocus=False)
    entry_var.set("")

# Button to reset the game
reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack(pady=10)

# Start the main event loop
root.mainloop()
