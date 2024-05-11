c = int(input("Press 1 to continue and 0 to exit calculator: "))
while(c!=0):
    print("Enter first number")
    a = int(input())
    print("Enter second number")
    b = int(input())
    print("Enter the calculation operator (+,-,*,/,0 to exit)")
    c = str(input())
    if(c=="+"):
        print(a+b)
    elif(c=="-"):
        print(a-b)
    elif(c=="*"):
        print(a*b)
    elif(c=="/"):
        print(a/b)
    elif(c=="0"):
        break
    else:
        print("Wrong Operator")
print("Thank You")