from tkinter import * 
import random
from tkinter import ttk


root = Tk()
root.title('Rock, Paper, Scissors Game')
root.geometry("500x600")
root.config(bg="white")

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# add images to a list
game_images = [rock, paper, scissors]
# pick random number between 0-2
pick_number = random.randint(0,2)
# show an image when program runs
image_label = Label(root, image=game_images[pick_number], border=0)
image_label.pack(pady=20)

# create spin function
def spin():
    pick_number = random.randint(0, 2)
    image_label.config(image=game_images[pick_number], border=0)

    if user_choice.get() == "Rock":
        user_choice_value = 0
    elif user_choice.get() == "Paper":
        user_choice_value = 1
    elif user_choice.get() == "Scissors":
        user_choice_value = 2

    if user_choice_value == 0:
        if pick_number == 0:
            win_lose_label.config(text="it's a tie. spin again.")
        elif pick_number == 1:
             win_lose_label.config(text="paper beats rock. you lose.")
        elif pick_number == 2:
             win_lose_label.config(text="rock smashes scissors.")
    
    if user_choice_value == 1:
        if pick_number == 1:
            win_lose_label.config(text="it's a tie. spin again.")
        elif pick_number == 0:
             win_lose_label.config(text="paper beats rock. you win.")
        elif pick_number == 2:
             win_lose_label.config(text="scissors cuts paper. you lose.")
    
    if user_choice_value == 2:
        if pick_number == 2:
            win_lose_label.config(text="it's a tie. spin again.")
        elif pick_number == 0:
             win_lose_label.config(text="rock smashes scissors. you lose.")
        elif pick_number == 1:
             win_lose_label.config(text="scissors cuts paper.")


# make choice
user_choice = ttk.Combobox(root, value=("Rock", "Paper", "Scissors"))
user_choice.current(0)
user_choice.pack(pady=10)


# create_button
spin_button = Button(root, text="Spin!", command=spin)
spin_button.pack(pady=10)


# label for showing whether you win or lose
win_lose_label = Label(root, text="", font=("Helvetica", 18))
win_lose_label.pack(pady=50)


root.mainloop()