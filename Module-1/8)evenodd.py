a,b=map(int, input("Enter your range=").split())
ce=0
co=0
for i in range(a,b+1):
    if i%2==0:
        print("Even Number=",i)
        ce+=1
    else:
        print("Odd number",i)
        co+=1
print("Count of even number=",ce)
print("Count of odd number=",co)
