message = input("Enter a message to encrypt: ")
if(len(message)>3):
    pop = message[0:1]
    message=message[1:]
    message=message+pop
    pre = input("Enter a random 3 letter text to encrypt: ")
    post = input("Enter a random 3 letter text to encrypt: ")
    pre=pre+message+post
    print(pre)
else:
    code = message[::-1]
    print(code)
