import tkinter as tk

# Create the main window
root = tk.Tk()
screen_w = 300
screen_h = 350
root.geometry(f"{screen_w}x{screen_h}")
root.resizable(False, False)
root.title("Tic, Tac, Toe by Vivek")

# Global variables
turn = "X"  # To keep track of whose turn it is
buttons = []  # To store the buttons
winning_buttons = []  # To store the winning buttons

# Function to handle button click
def click(i, j):
    global turn
    button = buttons[i * 3 + j]
    if button.cget('text') == "" and not win_check():  # Check if the button is empty and the game is not won
        button.config(text=turn)  # Set button text to X or O based on turn
        if turn == "X":
            turn = "O"
            label.config(text=f"{turn}'s Turn")  # Update status label
        else:
            turn = "X"
            label.config(text=f"{turn}'s Turn")  # Update status label
        check_draw()  # Check if the game is a draw
        check_winner()  # Check if there is a winner

# Function to check for win conditions
def win_check():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Row
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Column
        [0, 4, 8], [2, 4, 6]  # Diagonal
    ]
    for condition in win_conditions:
        if buttons[condition[0]].cget('text') == buttons[condition[1]].cget('text') == buttons[condition[2]].cget('text') != "":
            winning_buttons.extend([buttons[condition[0]], buttons[condition[1]], buttons[condition[2]]])
            return True
    return False

# Function to check for a winner
def check_winner():
    if win_check():
        winner = "X" if turn == "O" else "O"  # Determine the winner
        label.config(text=f"{winner} Wins")  # Update status label
        change_button_color()  # Change color of winning buttons

# Function to check for a draw
def check_draw():
    for button in buttons:
        if button.cget('text') == "":
            return False
    label.config(text="It's Draw!")  # Update status label

# Function to change color of winning buttons
def change_button_color():
    for button in winning_buttons:
        button.config(bg="light green")

# Function to reset the game
def reset():
    global turn
    for button in buttons:
        turn = "X"
        label.config(text=f"{turn}'s Turn")  # Reset status label
        button.config(text="", bg="SystemButtonFace")  # Reset buttons

# Creating buttons (board) and status label
for i in range(0, 3):
    for j in range(0, 3):
        button = tk.Button(root, width=7, height=3, font="Helvetica 17", command=lambda i=i, j=j: click(i, j))
        button.grid(row=i, column=j)
        buttons.append(button)

# Status label
label = tk.Label(root, text=f"{turn}'s Turn", font="Helvetica 15")
label.grid(row=3, column=0, pady=14)

# Reset button
reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.grid(row=3, column=2)

root.mainloop()
