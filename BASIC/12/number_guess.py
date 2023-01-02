numberguess = 10
guesscount = 0
guesslimit = 5

while guesscount < guesslimit:
    guess = int(input("guess secret number: >>> "))
    guesscount += 1
    if guess == numberguess:
        print("you have guessed the number.")
        break
else:
    print("please, play again.")