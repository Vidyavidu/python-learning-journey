import time

count = 10

while count >=1:
    print(count , end="\r")
    time.sleep(1)
    count -=1

print("Happy New Year!")