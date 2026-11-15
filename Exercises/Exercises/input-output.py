
# 1. Accept input from user and print the output 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

res = num1 * num2
print("The multiplication is:", res)

# 2.Using the sep parameter to join strings
print('Name', 'Is', 'James', sep='***')

#3.
num = 8
# Using %o to format the integer as octal
print('%o' % num)

#4. Binary representation
num = int(input("Enter a decimal number: "))
binary_val = f"{num:b}"

print(f"The binary representation of {num} is {binary_val}")

#5. Taking multiple inputs in one go
str1, str2, str3 = input("Enter three names: ").split()

print('Name1:', str1)
print('Name2:', str2)
print('Name3:', str3)

#6.Hexadecimal representation
num = int(input("Enter a number: "))
hex_val = f"{num:x}"

print(f"The hexadecimal value is {hex_val}")

#7.Display float number with 2 decimal places
num = 458.541315
print('%.2f' % num)

#8.Percentage display
num = int(input("Enter numerator: "))
den = int(input("Enter denominator: "))

percentage = (num / den) * 100
print(f"The result is: {percentage:.2f}%")

#9.Display right-aligned output
word = input("Enter a word: ")
version = input("Enter a version number: ")
print(f"{word:>20} {version}")

#10.Center-aligned text
title = "REPORT SUMMARY"
formatted_title = f"{title:-^40}"

print(formatted_title)

#11. Padding with zeros
val = input("Enter your ID number: ")

# Method 1: Using zfill
print(val.zfill(5))
# Method 2: Using f-string (requires integer)
# print(f"{int(val):05}")


#12: Format variables using string.format() method
quality = 4
totalmoney = 20
price = 5
statement = "I have {1}rs so i can buy only {0} chocolates of cost {2:.2f}rs."
print(statement.format(quality , totalmoney, price))