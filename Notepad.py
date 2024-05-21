import tkinter as tk
from tkinter import messagebox as msgbox
from tkinter import filedialog

# Basic setup
root = tk.Tk()
screen_w = 700
screen_h = 400
root.geometry(f"{screen_w}x{screen_h}")
root.title("Notepad by Vivek")

# Creating Frames
f0 = tk.Frame(root)
f1 = tk.Frame(root)
f2 = tk.Frame(root, relief="sunken")
f3 = tk.Frame(root)
# Packing Frames
f0.pack()
f1.pack()
f2.pack(side="bottom", fill="x")
f3.pack()

# Some variables
is_wrap = tk.IntVar()
page_wrap = "none"
file = None

def wrap():
    global page_wrap
    if is_wrap.get() == 0:
        print(is_wrap.get())
        page_wrap = "none"

    else:
        print(is_wrap.get())
        page_wrap = "char"

    page.config(wrap=page_wrap)

def update_character_count(event=None):
    num_of_char = len(page.get("1.0", "end-1c"))
    char_count_label.config(text=f"{num_of_char} Characters")
def get_cursor_pos(event=None):
    cursor_pos = page.index("insert").replace(".",",")
    cursor_pos_label.config(text=f"Cursor Position {cursor_pos}")

def new_file(event=None):
    page.delete(1.0, "end")
    char_count_label.config(text="No. of characters: ")
    filename.config(text="Untitled")

def open_file(event=None):
    global file
    file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        with open(file, "r") as f:
            page.delete(1.0, "end")
            page.insert(1.0, f.read())
        filename.config(text=file)

def save_file(event=None):
    global file
    file = filedialog.asksaveasfilename(initialfile="Untitled", defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    if not file == "":
        with open(str(file), "w") as f:
            f.write(page.get(1.0, "end"))

def cut(event=None):
    page.event_generate("<<Cut>>")
def copy(event=None):
    page.event_generate("<<Copy>>")
def paste(event=None):
    page.event_generate("<<Paste>>")

def font_size():
    if type.get() == "None":
        page.config(font=f"{style.get()} {value.get()}")
    else:
        page.config(font=f"{style.get()} {value.get()} {type.get().lower()}")

def font_type():

    if type.get() == "None":
        page.config(font=f"{style.get()} {value.get()}")

    else:
        page.config(font=f"{style.get()} {value.get()} {type.get().lower()}")

def font_style():
    if type.get() == "None":
        page.config(font=f"{style.get()} {value.get()}")
    else:
        page.config(font=f"{style.get()} {value.get()} {type.get().lower()}")

def bold(event=None):
    type.set("Bold")
    page.config(font=f"{style.get()} {value.get()} {type.get().lower()}")

def italic(event=None):
    type.set("Italic")
    page.config(font=f"{style.get()} {value.get()} {type.get().lower()}")

def underline(event=None):
    type.set("Underline")
    page.config(font=f"{style.get()} {value.get()} {type.get().lower()}")

def about():
    msgbox.showinfo("About Notepad", "Notepad is a simple text editor by Vivek")

# Menubar
menubar = tk.Menu(f1)

# File menu
m1 = tk.Menu(menubar, tearoff=0)
m1.add_command(label="New", command=new_file, accelerator="    Ctrl+N")
m1.add_command(label="Open", command=open_file, accelerator="    Ctrl+O")
m1.add_command(label="Save", command=save_file, accelerator="    Ctrl+S")
m1.add_separator()
m1.add_command(label="Exit", command=quit, accelerator="    Ctrl+Q")
menubar.add_cascade(label="File", menu=m1)

# Edit menu
m2 = tk.Menu(menubar, tearoff=0)
m2.add_command(label="Cut", command=cut, accelerator="    Ctrl+X")
m2.add_command(label="Copy", command=copy, accelerator="    Ctrl+C")
m2.add_command(label="Paste", command=paste, accelerator="    Ctrl+V")
m2.add_separator()
# Font menu Inisde Edit menu
fontmenu = tk.Menu(m2, tearoff=0)
sizemenu = tk.Menu(fontmenu, tearoff=0)
value = tk.IntVar()
value.set(11)
for i in range(11, 40, 2):
    sizemenu.add_radiobutton(label=i, variable=value, command=font_size)

# Font style menu
stylemenu = tk.Menu(fontmenu, tearoff=0)
style = tk.StringVar()
names = ["Arial", "Algerian", "Calibri", "Courier", "Garamond", "Helvetica", "Modern", "Roman", "Script", "Terminal"]
style.set("Calibri")

for name in names:
    stylemenu.add_radiobutton(label=name, variable=style, command=font_style)

# Font type menu
typemenu = tk.Menu(fontmenu, tearoff=0)
type = tk.StringVar()
typemenu.add_radiobutton(label="None", variable=type, command=font_type)
typemenu.add_radiobutton(label="Bold", variable=type, command=font_type, accelerator="    Ctrl+B")
typemenu.add_radiobutton(label="Italic", variable=type, command=font_type, accelerator="    Ctrl+I")
typemenu.add_radiobutton(label="Underline", variable=type, command=font_type, accelerator="    Ctrl+U")
type.set("None")

# Sub menu fo font menu
fontmenu.add_cascade(menu=sizemenu, label="Size")
fontmenu.add_cascade(menu=stylemenu, label="Style")
fontmenu.add_cascade(menu=typemenu, label="Type")

m2.add_cascade(menu=fontmenu, label="Font")

menubar.add_cascade(label="Edit", menu=m2)

# View menu
m3 = tk.Menu(menubar, tearoff=0)
m3.add_checkbutton(label="Wrap text", variable=is_wrap, command=wrap)
menubar.add_cascade(label="View", menu=m3)

# Help menu
m4 = tk.Menu(menubar, tearoff=0)
m4.add_command(label="About Notepad", command=about)
menubar.add_cascade(label="Help", menu=m4)

# Displaying menubar
root.config(menu=menubar)

# Vertical scrollbar
sb = tk.Scrollbar(f3)
sb.pack(side="right", fill="y")

# Horizontal scrollbar
sb2 = tk.Scrollbar(f3, orient="horizontal")
sb2.pack(side="bottom", fill="x")

# Text area
page = tk.Text(f3, font=f"Calibri 11", width=screen_w, height=screen_h, wrap=page_wrap)
page.pack(fill="both")

# Displaying Scrollbar
page.config(yscrollcommand=sb.set)
page.config(xscrollcommand=sb2.set)
sb.config(command=page.yview)
sb2.config(command=page.xview)

# Number of Characters
char_count_label = tk.Label(f2, text="Characters")
char_count_label.pack(side="left")
page.bind("<KeyRelease>", update_character_count)

# Cursor Position
cursor_pos_label = tk.Label(f2, text="Line, Column")
cursor_pos_label.pack(side="left", padx=40)
page.bind("<Key>", get_cursor_pos)
page.bind("<Button-1>", get_cursor_pos)

# Displaying current file name
filename = tk.Label(f2, text="Untitled")
filename.pack(side="left", padx=40)

# Shortcut keys
root.bind("<Control-n>", new_file)
root.bind("<Control-o>", open_file)
root.bind("<Control-s>", save_file)
root.bind("<Control-q>", quit)
root.bind("<Control-x>", cut)
root.bind("<Control-c>", copy)
root.bind("<Control-v>", paste)
root.bind("<Control-b>", bold)
root.bind("<Control-i>", italic)
root.bind("<Control-u>", underline)

root.mainloop()