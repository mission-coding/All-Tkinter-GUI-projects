import tkinter as tk
from tkinter import messagebox
import random

# Create the main window
root = tk.Tk()
screen_w = 380
screen_h = 360
root.geometry(f"{screen_w}x{screen_h}")
root.resizable(False, False)
root.title("Typing Test by Vivek")

# List of paragraphs for the typing test
paras = [
    "He wished he could go back and learn to find the excitement that came with change but it was useless.",
    "She could hear her mom yelling in the background, but couldn't make out exactly what the yelling was about.",
    "It was that terrifying feeling you have as you tightly hold the covers over you with the knowledge that there is something hiding under your bed.",
    "The warning signs had been ignored in favor of the possibility, however remote, that it could actually happen."
    ]

# Select a random paragraph
para = paras[random.randint(0, len(paras)-1)]
error = 0
speed = 0
time_stop = True
time_taken = 0

# Function to calculate errors and speed after typing
def errors_and_speed(event=None):
    global error, time_stop, speed

    para_text = para_widget.get(1.0, "end")
    ans_text = ans_widget.get(1.0, "end")

    para_words = para_text.split()
    ans_words = ans_text.split()
    for i in range(0, len(para_text.split())):
        try:
            if para_words[i] != ans_words[i]:
                error += 1
        except:
            error += 1

    time_stop = True

    # Calculate typing speed
    words = ans_text.split()
    speed = len(words)//(time_taken/60)
    
    # Show the result in a message box
    messagebox.showinfo("Result", f"Time Taken: {time_taken} seconds\nErrors: {error}\nSpeed: {speed} wpm")

# Function to start the typing test
def start():
    global time_stop
    para = paras[random.randint(0, len(paras)-1)]
    ans_widget.config(state="normal")
    para_widget.config(state="normal")
    para_widget.insert(1.0, para)
    para_widget.config(state="disabled")
    ans_widget.bind("<Button-1>", total_time)
    ans_widget.bind("<Return>", errors_and_speed)
    time_stop = False

# Function to calculate total time elapsed
def total_time(event=None):
    global time_taken
    if time_stop != True:
        time_taken += 1
        time_taken_label.config(text=f"Time Taken: {time_taken}")
        root.after(1000, total_time, time_taken)

# Function to reset the typing test
def reset():
    global time_taken, speed, error, time_stop, pa 
    time_taken=0
    para = paras[random.randint(0, len(paras)-1)]
    speed=0
    error=0
    time_stop = True
    time_taken_label.config(text="Time Taken: ")
    para_widget.config(state="normal")
    para_widget.delete(1.0, "end")
    para_widget.config(state="disabled")
    ans_widget.delete(1.0, "end")
    ans_widget.config(state="disabled")

# Paragraph label and widget
tk.Label(root, text="Paragraph").pack(pady=5)
para_widget = tk.Text(root, relief="sunken", height=8, wrap="word")
para_widget.config(state="disabled")
para_widget.pack(fill="both", expand=True)

# Text entry label and widget
tk.Label(root, text="Type the above Paragraph here").pack(pady=5)
ans_widget = tk.Text(root, height=8, relief="sunken", wrap="word")
ans_widget.config(state="disabled")
ans_widget.pack(fill="both", expand=True)

# Start button
start_button = tk.Button(root, text="Start Typing Test", command=start)
start_button.pack(side="right", padx=5, pady=5)

# Reset button
reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack(side="right", padx=5, pady=5)

# Label to display time taken
time_taken_label = tk.Label(root, text="Time Taken: ")
time_taken_label.pack(side="left", padx=5, pady=5)

# Start the main event loop
root.mainloop()
