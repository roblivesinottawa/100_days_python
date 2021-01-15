print("Welcome to Python Pizza Delivery!")
size = input("what size of pizza do you want? S, M, L? \n")
pepperoni = input("do you want to add pepperoni? Y or N? \n")
extra_cheese = input("do you want to add extra cheese? Y or N? \n")
tip = input("would you like to add a tip? Y or N \n")
tip_value = float(input("How much would you like to tip? 10, 12 or 15? \n"))

bill = 0


if size == "S":
  bill += 15
elif size == "M":
  bill += 20 
else:
  bill += 25

if pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == 'Y':
    bill += 1

if tip == 'Y':
    bill = bill + tip_value / 100
  
# find a way to express in code if the user does not want to tip


print(f"your total is ${bill}")