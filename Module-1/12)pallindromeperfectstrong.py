a=int(input("Enter your number="))
original=a
rever=0
while (a!=0):
        rer = a % 10
        rever = rever * 10 + rer
        a/= 10
if original==rever:
    print("Pallindrome")
else:
    print("Not Pallindrome")        

