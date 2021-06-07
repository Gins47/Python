status = ""
started = False
while status.lower() != "quit":
    status = input(f"Enter the command ")
    if status == "start":
        if started == True:
            print("Car already started")
        else:
            started = True
            print("car started")
    elif status == "stop":
        if started == False:
            print("Car already stopped")
        else:
            started = False
            print("car stopped")
    elif status == "quit":
        break
    else:
        print("invalid command")
