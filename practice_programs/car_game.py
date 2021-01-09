direction = ""
started = False

while True:
    direction = input("enter command: >>> ").lower()

    if direction == 'start':
        if started:
            print("car is already started...")
        else:
            started = True
            print("car started...")
    elif direction == 'stop':
        if not started:
            print("car is already stopped...")
        else:
            started = False
            print("car stopped...")
    elif direction == 'help':
        print("""
        type 'start' to start vehicle
        type 'stop' to stop vehicle
        type 'quit' to quit
        """)
    elif direction == 'quit':
        break
    else:
        print("sorry. choose another command.")
