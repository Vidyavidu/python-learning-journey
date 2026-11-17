#18.Read a file and store its content in a list
with open("test.txt","r") as f:
    lines = f.readlines()
    print(lines)


#19.Write list of strings to a file
fruits_list = ["Apple", "Banana","watermelon","mango","cherry","Date"]

with open ("fruits.txt","w") as f:
    for fruit in fruits_list:
        f.write(fruit+"\n")
        
print(" file fruits.txt has been succesfully created!")

#20.Count total lines in a file
line_count = 0
 
with open("sample.txt","r") as f:
    for line in f:
        line_count +=1

print(f"The total number of lines is {line_count}")

#21.Read line number 4 from a file
with open("test.txt" , "r") as f:
    lines = f.readlines()
    print(lines[3])


