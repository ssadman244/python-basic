print("""
**********   Car Game  **********
    start - Start the car
    stop - Stop the car
    quit - to exit
""")
is_started = False
while True:
    inp = input("> ").lower()
    if inp == "start":
        if not is_started:
            print("Car started, ready to go!")
        else:
            print("Car already started!")
        is_started = True
    elif inp == "stop":
        if not is_started:
            print("Car already stopped!")
        else:
            print("Car stopped.")
        is_started = False
    elif inp == "quit":
        break
    else:
        print("Oops! Something wrong.")
