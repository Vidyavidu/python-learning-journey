Time = int(input("Enter the time(1-12):"))
period = input("AM OR PM?:") .strip().upper()

if period =="AM":
    if Time <6:
        print("Its sleeping time!")
    elif Time <8:
        print("get ready and work")
    elif Time<10:
        print("its breakfast time")
    else:
        print("its study time")

elif period=="PM":
    if Time <5:
        print("its study time")
    elif Time <6:
        print("its play time")
    elif Time <8:
        print("its dinner time")
    else:
        print("its sleep time")

else:
    print("its invalid input")

 

