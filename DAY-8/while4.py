available_seats = 8

while available_seats >0:
   print(f"{available_seats} seats available")
   booking = input("do you want to book a seat? (yes/no):").lower()

   if booking == "yes":
    available_seats -=1
    print("seat booked!")
   else:
    print("no booking done! good bye")
    break

if available_seats==0:
 print("all seats are booked")
 