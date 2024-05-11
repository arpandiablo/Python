import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
if(int(time.strftime("%H"))<12):
    print("Good Morning")
elif(int(time.strftime("%H"))>12 and int(time.strftime("%H"))<17):
    print("Good Afternoon")
else:
    print("Good Evening")