secretnumber = 5
guesscount = 0
guesslimit = 3

while guesscount < guesslimit:
    guess = int(input("enter guessed number: >>> "))
    guesscount += 1
    if guess == secretnumber:
        print("you've guessed it right.")
        break
else:
    print("try again")