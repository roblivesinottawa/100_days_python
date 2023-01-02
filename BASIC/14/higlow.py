import time, random

ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["Clubs", "Hearts", "Diamonds", "Spades"]
deck = []

value = 1
for rank in ranks:
    for suit in suits:
        deck.append([rank + " of " + suit, value])
    value = value + 1

random.shuffle(deck)
score = 0
card_one = deck.pop(0)

while True:
    # os.system("cls")
    print(f"your score so far is {score}")
    print(f"the current card is {card_one[0]}")
    while True:
        choice = input("higher or lower? ")
        if len(choice) > 0:
            if choice[0].lower() in ["h", "l"]:
                break

    
    card_two = deck.pop(0)
    print(f"the next picked card is {card_two[0]}")
    time.sleep(1)

    if choice[0].lower() == 'h' and card_two[1] > card_one[1]:
        print("correct!")
        score += 1
        time.sleep(1)
    elif choice[0].lower() == 'l' and card_two[1] < card_one[1]:
        print("wrong!")
        time.sleep(1)
        break
    elif choice[0].lower() == 'l' and card_two[1] < card_one[1]:
        print("correct!")
        score += 1
        time.sleep(1)
    elif choice[0].lower() == 'l' and card_two[1] > card_one[1]:
        print("wrong!")
        time.sleep(1)
        break
    else:
        print("draw!")

    car_one = card_two

# os.system("cls")
print("game over!")
print(f"your final score is {score}")
time.sleep(4)
# os.system("cls")