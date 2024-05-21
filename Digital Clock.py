from tkinter import Tk, Label
import time

root = Tk()
screen_w = 325
screen_h = 70
root.geometry(f"{screen_w}x{screen_h}")
root.resizable(width=False, height=False)
root.title('Digital Clock by Vivek')

def upadte_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, upadte_time)

time_label = Label(root, font="Courier 50", fg="green", bg="black")
time_label.pack()

upadte_time()

root.mainloop()