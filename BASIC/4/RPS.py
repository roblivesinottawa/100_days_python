import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("type 0 for rock, 1 for paper or 2 for scissors. \n"))
if user_choice >= 3 or user_choice < 0:
  print("you chose a number out of range, please try again.")
else:
  print(game_images[user_choice])

  computer_choice = random.randint(0, 2)
  print(f"computer chose: ")
  print(game_images[computer_choice])

  # how can we compare these two choices.
  if user_choice == 0 and computer_choice == 2:
    print("you win!")
  elif computer_choice == 0 and user_choice == 2:
    print("you lose.")
  elif computer_choice > user_choice:
    print("you lose.")
  elif user_choice > computer_choice:
    print("you win!")
  elif computer_choice == user_choice:
    print("it's a draw.")