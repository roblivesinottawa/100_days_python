from random import randint

EASY_LEVEL = 5
HARD_LEVEL = 10

def answerchecker(guess, answer, turns):
    if guess > answer:
        print("you went too high there.")
        return turns -1
    elif guess < answer:
        print("now you went too low there.")
        return turns -1
    else:
        print(f"you got it. the answe was {answer} congrats!")

def difficultsetter():
    level = input("please select level: type 'easy' or 'hard': >>> ")
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print("welcome to the number guess game")
    print("I'm thinking of a number from 1-100")
    answer = randint(1, 100)
    # print(f"the correct number is {answer}")

    turns = difficultsetter()

    guess = 0
    while guess != answer:
        print(f"you have {turns} remaining.")

        guess = int(input("please make a guess: >>> "))
        
        turns = answerchecker(guess, answer, turns)

        if turns == 0:
            print("you have run out of tries. play again.")
            return
        elif guess != answer:
            print("guess again.")


game()
