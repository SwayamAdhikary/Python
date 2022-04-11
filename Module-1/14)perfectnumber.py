from re import I


n=int(input("Enter your number="))
s=0
for i in range (1,n):
    if n%i==0:
        s=s+i
if s==n:
    print("Perfect Number")
else:
    print("Not perfect number")