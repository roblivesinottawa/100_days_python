# insert ascii art here

print("WELCOME TO TREASURE ISLAND")
print("your mission is to find the treasure.")

choice_one = input("your're at a crossroads, where do you want to go? Type 'left' or 'right'. >>> ").lower()

if choice_one == "left":
  choicetwo = input("proceed. type 'wait' to wait for a boat or 'swim' to swim across. >>> ").lower()
  if choicetwo == 'wait':
    choicethree = input("you are unharmed. there is a house with three doors. one is red, the other is yellow and the last one is blue. which color do you choose? >>> ").lower()
    if choicethree == 'red':
      print("you're burning. game over.")
    elif choicethree == 'yellow':
      print("you find the treasure. you win.")
    elif choicethree == 'blue':
      print("you froze. game over.")
    else:
      print("you choose a door that does not exist. game over.")

  else:
    print('you drowned. game over. ')
else:
  print("you fell into a hole. game over.")