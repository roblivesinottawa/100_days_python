wordList = ['fuck', 'shit', 'ass', 'motherfucker', 'butthole']

import random
word = random.choice(wordList)

# line test
print(f"the solution is {word}")

display = []
wordlength = len(word)
for _ in range(wordlength):
  display += "_"


guess = input("can you guess a letter? >>> ").lower()

for position in range(wordlength):
  letter = word[position]
  if letter == guess:
    display[position] = letter

print(display)