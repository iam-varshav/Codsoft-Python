import string
import random
pswdlen=int(input("Enter the length of the password: "))
print("Choose character : 1. Digits 2. Letters 3. Special Characters 4. Exit" )
list=""
while(True):
    choice=int(input("Choose a character: "))
    if(choice==1):
        list+=string.ascii_letters
    elif(choice==2):
        list+=string.digits
    elif(choice==3):
        list+=string.punctuation
    elif(choice==4):
        break
    else:
        print("Choose valid Character")
password=[]
for i in range (pswdlen):
    randomchar=random.choice(list)
    password.append(randomchar)
print("The random password is " + "".join(password))
