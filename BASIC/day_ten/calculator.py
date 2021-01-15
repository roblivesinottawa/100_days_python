def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

should_continue = True

while should_continue:
    print("""please select operation: 
    '1. Add'
    '2. Subtract'
    '3. Multiply'
    '4. Divide'
    """)

    select = float(input("select operations from 1, 2, 3, 4: "))

    number_one = float(input("enter first number >>> "))
    number_two = float(input("enter second number >>> "))


    if select == 1:
        print(f"{number_one} + {number_two} = {add(number_one, number_two)}")
    elif select == 2:
        print(f"{number_one} - {number_two} = {subtract(number_one, number_two)}")
    elif select == 3:
        print(f"{number_one} * {number_two} = {multiply(number_one, number_two)}")
    elif select == 4:
        print(f"{number_one} / {number_two} = {divide(number_one, number_two)}")
    else:
        print("invalid input")

    continue_ = input("type 'c' to continue or 'q' to quit: ")
    print(continue_)

    if continue_ == 'c':
        should_continue = True
    else: 
        should_continue = False