import random
from hangmanwords import wordlist
from hangmanart import logo, stages

word = random.choice(wordlist)
wordlength = len(word)

endgame = False
lives = 6

print(logo)

# create blanks
display = []
for _ in range(wordlength):
  display += "_"


while not endgame:
    guess = input("can you guess a letter? >>> ").lower()

    if guess in display:
        print(f"you've already guessed {guess}")
    # check guessed letter
    for position in range(wordlength):
        letter = word[position]
        # print(f"current position: {position}\n current letter: {letter}\n guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in word:
        print(f"you guessed {guess}, that's not in the word. you lose a life.")
        lives -= 1
        if lives == 0:
            endgame = True
            print("you lose.")

    # join all the elements into a string
    print(f"{' '.join(display)}")

    # check if user got all the letters
    if "_" not in display:
        endgame = True
        print("you win.")

    print(stages[lives])