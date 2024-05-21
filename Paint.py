import tkinter as tk
from tkinter import ttk

root = tk.Tk()
screen_w = 700
screen_h = 450
# root.geometry(f"{screen_w}x{screen_h}")
root.title("Paint by Vivek")
pre_x = None
pre_y = None
selected_tool = "pen"

def new_file():
    pass
def open_file():
    pass
def save_file():
    pass

def pen():
    global selected_tool
    selected_tool="pen"

def erase():
    global selected_tool
    selected_tool="erase"

def draw(event):
    global pre_x, pre_y
    if selected_tool == "pen":
        if pre_x is not None and pre_y is not None:
            canvas.create_line(pre_x, pre_y, event.x, event.y, fill=pen_color.get(), width=pen_size.get(), smooth=True)
        pre_x = event.x
        pre_y = event.y
    else:
        if pre_x is not None and pre_y is not None:
            canvas.create_line(pre_x, pre_y, event.x, event.y, fill="white", width=eraser_size.get(), smooth=True)
        pre_x = event.x
        pre_y = event.y

def release(event):
    global pre_x, pre_y
    pre_x = None
    pre_y = None

def clear():
    canvas.delete("all")


# Canvas
canvas = tk.Canvas(root, bg="white", width=screen_w, height=screen_h)
canvas.pack(side="left", fill="both", expand=True)

# # Menubar
# menubar = tk.Menu(root)
# filemenu = tk.Menu(menubar, tearoff=0)
# filemenu.add_command(label="New", command=new_file)
# filemenu.add_command(label="Open", command=open_file)
# filemenu.add_command(label="Save", command=save_file)
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=quit)
# menubar.add_cascade(menu=filemenu, label="File")
# root.config(menu=menubar)

# Tool Frame
tool_frame = tk.LabelFrame(root, text="Tools", padx=10)
tool_frame.pack(side="right", fill="y", padx=10, pady=10)

# Pen
pen_button = ttk.Button(tool_frame, text="Pen", command=pen)
pen_button.pack(padx=5, pady=5)

# Eraser
eraser_button = ttk.Button(tool_frame, text="Eraser", command=erase)
eraser_button.pack(padx=5, pady=5)

# Clear all
clear_button = ttk.Button(tool_frame, text="Clear All", command=clear)
clear_button.pack(padx=5, pady=5)

# Pen Colors
tk.Label(tool_frame, text="Pen Color").pack(pady=5)
colors = ["Black", "White", "Red", "Yellow", "Green", "Blue", "Purple", "Orange", "Pink", "Grey"]
pen_color = ttk.Combobox(tool_frame, values=colors, state="readonly")
pen_color.current(0)
pen_color.pack(padx=5, pady=5)

# Pen Size
tk.Label(tool_frame, text="Pen size").pack(pady=5)
pen_size = ttk.Scale(tool_frame, from_=1, to=12)
pen_size.set(3)
pen_size.pack()

# Eraser Size
tk.Label(tool_frame, text="Eraser size").pack(pady=5)
eraser_size = ttk.Scale(tool_frame, from_=1, to=20)
eraser_size.set(5)
eraser_size.pack()

canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", release)

root.mainloop()

