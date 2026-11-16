# 13.Currency formatting with commas
num = float(input("Enter a number : "))

balance = f"${num:,.2f}"
print(f"Total Balace : {balance}")


#14.Accept a list of 5 float numbers
numbers = []

for i in range(0,5):
    print("Enter the number in the location :" , i)
    item = float(input())
    numbers.append(item)
    
print("User list : ", numbers)


#15.Tabular output from lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

print(f"{'Name':<10} {'Score'}")
print("-"*15)

for names , scores in zip(names , scores):
    print(f"{names:<10} {scores}")


#16.Interactive menu

menu = int(input("Enter the number (1-3) : "))

if menu==1:
    print("1.Hey there!")
elif menu==2:
    num = int(input("Enter a number : "))
    print(f"Suare of {num} is {num*num}")
elif menu==3:
    print("Thank you bye!")
else:
    print("Invalid input")

#17. Password hiding 
import getpass

user = input("Enter username : ")
pwd = getpass.getpass ("Enter password:")

if user=="admin" and pwd == "vidya@123":
 print("Login successful!")
else:
    print("Access denied!")

#or

import pwinput

user = input("Enter username : ")
pwd = pwinput.pwinput("Enter password : " , mask="*")

if user=="admin" and pwd=="vidya@123":
    print("Login succesfull!")
else:
    print("Access denied")


