import tkinter as tk
from math import *

root = tk.Tk()
screen_w = 250
screen_h = 360
root.geometry(f"{screen_w}x{screen_h}")
root.title("Calculator by Vivek")
root.resizable(width=False, height=False)
#root.config(background="grey")

boxval = tk.StringVar()
# boxval.set("")

box = tk.Entry(root, textvariable=boxval, width=16, font="Helvetica 20")
box.grid(row=0, column=6)
box = tk.Entry(root, textvariable=boxval, width=18, font="Helvetica 20")
box.place(x=0, y=0)


def click(text):
    text = text
    global boxval

    if text == "C":
        boxval.set("")

    # elif text == "sq":
    #     boxval.set(float(boxval.get())**2)

    elif text == "=":
        if boxval.get().isdigit():
            value = int(boxval.get())
        else:
            try:
                boxval.set(eval(boxval.get()))
            except:
                if boxval.get() != "":
                    boxval.set("Error")

    # elif text == "√":
    #     boxval.set(sqrt(float(boxval.get())))

    elif text == "x":
        boxval.set(boxval.get()[:-1])

    else:
        boxval.set(boxval.get() + text)
        box.update()

tk.Button(root, text="(", font="Helvetica 11", width=6, height=4, relief="sunken", command=lambda: click("(")).place(x=0,y=35)
tk.Button(root, text=")", font="Helvetica 11", width=6, height=4, relief="sunken", command=lambda: click(")")).place(x=screen_w/4,y=35)
tk.Button(root, text="C", font="Helvetica 11", width=6, height=4, relief="sunken", command=lambda: click("C")).place(x=screen_w/2,y=35)
tk.Button(root, text="+", font="Helvetica 11", width=6, height=4, relief="sunken", command=lambda: click("+")).place(x=screen_w/1.33,y=35)
tk.Button(root, text="1", font="Helvetica 11", width=6, height=4, relief="sunken", command=lambda: click("1")).place(x=0,y=(screen_h-35)/3.3)
tk.Button(root, text="2", font="Helvetica 11", width=6, height=4, relief="sunken", command=lambda: click("2")).place(x=screen_w/4,y=(screen_h-35)/3.3)
tk.Button(root, text="3", font="Helvetica 11", width=6, height=4, relief="sunken", command=lambda: click("3")).place(x=screen_w/2,y=(screen_h-35)/3.3)
tk.Button(root, text="-", font="Helvetica 11", width=6, height=4, relief="sunken", command=lambda: click("-")).place(x=screen_w/1.33,y=(screen_h-35)/3.3)
tk.Button(root, text="4", font="Helvetica 11", width=6, height=4, relief="sunken", command=lambda: click("4")).place(x=0,y=(screen_h-35)/1.975)
tk.Button(root, text="5", font="Helvetica 11", width=6, height=4, relief="sunken", command=lambda: click("5")).place(x=screen_w/4,y=(screen_h-35)/1.975)
tk.Button(root, text="6", font="Helvetica 11", width=6, height=4, relief="sunken", command=lambda: click("6")).place(x=screen_w/2,y=(screen_h-35)/1.975)
tk.Button(root, text="*", font="Helvetica 11", width=6, height=4, relief="sunken", command=lambda: click("*")).place(x=screen_w/1.33,y=(screen_h-35)/1.975)
tk.Button(root, text="7", font="Helvetica 11", width=6, height=4, relief="sunken", command=lambda: click("7")).place(x=0,y=(screen_h-35)/1.4055)
tk.Button(root, text="8", font="Helvetica 11", width=6, height=4, relief="sunken", command=lambda: click("8")).place(x=screen_w/4,y=(screen_h-35)/1.4055)
tk.Button(root, text="9", font="Helvetica 11", width=6, height=4, relief="sunken", command=lambda: click("9")).place(x=screen_w/2,y=(screen_h-35)/1.4055)
tk.Button(root, text="/", font="Helvetica 11", width=6, height=4, relief="sunken", command=lambda: click("/")).place(x=screen_w/1.33,y=(screen_h-35)/1.4055)
tk.Button(root, text="x", font="Helvetica 11", width=6, height=4, relief="sunken", command=lambda: click("x")).place(x=0,y=(screen_h-35)/1.095)
tk.Button(root, text="0", font="Helvetica 11", width=6, height=4, relief="sunken", command=lambda: click("0")).place(x=screen_w/4,y=(screen_h-35)/1.095)
tk.Button(root, text=".", font="Helvetica 11", width=6, height=4, relief="sunken", command=lambda: click(".")).place(x=screen_w/2,y=(screen_h-35)/1.095)
tk.Button(root, text="=", font="Helvetica 11", width=6, height=4, relief="sunken", bg="light green",command=lambda: click("=")).place(x=screen_w/1.33,y=(screen_h-35)/1.095)
 

root.mainloop()

