import math
n=int(input("Enter your number="))
s=str(n)
j=0
for i in s:
    j+=math.factorial(int(i))
if j==n:
    print("Strong Number")
else:
    print("Not strong number")