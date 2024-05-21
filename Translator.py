import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import pygame
from io import BytesIO

# Create the main window
root = tk.Tk()
screen_w = 460
screen_h = 210
root.geometry(f"{screen_w}x{screen_h}")
root.resizable(False, False)
root.title("Translator by Vivek")

# Initialize the translator and get the list of supported languages
translator = Translator()
languages = list(LANGUAGES.values())

# Create and position the comboboxes for selecting languages
from_combobox = ttk.Combobox(root, values=languages, width=30)
from_combobox.place(x=10, y=2)
from_combobox.current(21)  # Set a default language

to_combobox = ttk.Combobox(root, values=languages, width=30)
to_combobox.place(x=screen_w/2+15, y=2)
to_combobox.current(38)  # Set a default language

# Create and position the text widgets for input and output
from_text = tk.Text(root, width=25, height=9, font="Arial 11")
from_text.place(x=10, y=25)

to_text = tk.Text(root, width=25, height=9, state="disabled", font="Arial 11")
to_text.place(x=screen_w/2+15, y=25)

# Function to perform translation
def trans(event=None):
    translation = translator.translate(
        text=from_text.get(1.0, "end-1c"),
        dest=to_combobox.get(),
        src=from_combobox.get()
    )
    to_text.config(state="normal")
    to_text.delete(1.0, "end")
    to_text.insert("end", translation.text)
    to_text.config(state="disabled")

# Function to play the text as speech
def play_text(text_widget):
    text = text_widget.get(1.0, "end-1c")
    tts = gTTS(text=text, lang='en')
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()

# Function to interchange languages
def interchange():
    from_combobox_set = languages.index(to_combobox.get())
    to_combobox_set = languages.index(from_combobox.get())
    from_combobox.current(from_combobox_set)
    to_combobox.current(to_combobox_set)

# Create and position the translation button
trans_button = tk.Button(root, text="Translate", command=trans)
from_text.bind("<Return>", trans)
trans_button.place(x=screen_w/2-30, y=screen_h-30)

# Create and position the play buttons for input and output text
play_from_button = tk.Button(root, text="Play", command=lambda: play_text(from_text))
play_from_button.place(x=screen_w/4-20, y=screen_h-30)

play_to_button = tk.Button(root, text="Play", command=lambda: play_text(to_text))
play_to_button.place(x=3*screen_w/4-20, y=screen_h-30)

# Create and position the interchange button
tk.Button(root, text="⇄", command=interchange).place(x=screen_w/2-12, y=0)

# Create and position the arrow label
tk.Label(root, text="→", font="Arial 14 bold").place(x=screen_w/2-12, y=screen_h/2)

# Start the main event loop
root.mainloop()
