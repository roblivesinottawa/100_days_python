import random

letters = ['a', 'b', 'c', 'd', 'e', 'f',  'g', 'h', 'i', 'j', 
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
'v', 'w', 'x', 'y', 'z',  'A', 'B', 'C', 'D', 'E', 'F', 'G', 
'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [ '0', '1', '2', '3', '4', '5', '6', '7', '8',  '9']
symbols = [ '!', '@', '#', '$', '%', '^', '&', '*']


print("Password Generator")

lettercount = int(input("how many letters would you like in your password? >>>"))
numbercount = int(input("how many numbers would you like in your password? >>>"))
symbolcount = int(input("how many symbols would you like in your password? >>>"))

password = []

for _pass in range(lettercount):
    password.append(random.choice(letters))
for _pass in range(numbercount):
    password += random.choice(numbers)
for _pass in range(symbolcount):
    password += random.choice(symbols)
random.shuffle(password)


_password = ""
for _pass in password:
    _password += _pass
print(_password)