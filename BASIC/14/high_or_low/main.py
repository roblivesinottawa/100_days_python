from art import logo, vs
from gamedata import data   
import random


def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description} from {account_country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        if guess == "a":
            return True
        else:
            return False




print(logo)
score = 0
should_continue = True
account_b = random.choice(data)

while should_continue:
    account_a = account_b
    account_b = random.choice(data)
    
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("who has more followers? Type 'A' or 'B': ").lower()

    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]

    correct = check_answer(guess, follower_count_a, follower_count_b)

    
   
    print(logo)
    if correct:
        score += 1
        print(f"you got it! the current score is {score}.")
    else:
        should_continue = False
        print(f"sorry, that's not right. the final score is {score}.")
