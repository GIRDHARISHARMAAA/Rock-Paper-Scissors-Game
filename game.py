import tkinter as tk
from tkinter import messagebox
import random



def play(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    result_label.config(text=f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result =  "You win!"
    else:
        result = "You lose!"

    messagebox.showinfo("Result", result)

def reset():
    result_label.config(text="Make your choice!")

def exit_game():
    root.destroy()

# Set up the main tkinter window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x300")
root.resizable(False, False)

# Add a title label
title_label = tk.Label(root,bg="orange", text="Rock, Paper, Scissors", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Add a label to display the result
result_label = tk.Label(root, text="Make your choice!", font=("Arial", 14))
result_label.pack(pady=20)

# Add buttons for Rock, Paper, Scissors
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock",bg="aqua", font=("Arial", 12), width=10, command=lambda: play('Rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper",bg="aqua", font=("Arial", 12), width=10, command=lambda: play('Paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors",bg="aqua", font=("Arial", 12), width=10, command=lambda: play('Scissors'))
scissors_button.grid(row=0, column=2, padx=10)

# Add Reset and Exit buttons
control_frame = tk.Frame(root)
control_frame.pack(pady=20)

reset_button = tk.Button(control_frame, text="Reset",bg="yellow", font=("Arial", 12), width=10, command=reset)
reset_button.grid(row=0, column=0, padx=10)

exit_button = tk.Button(control_frame, text="Exit",bg="red", font=("Arial", 12), width=10, command=exit_game)
exit_button.grid(row=0, column=1, padx=10)

# Run the tkinter main loop
root.mainloop()
