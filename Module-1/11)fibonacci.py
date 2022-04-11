a=0
b=1
r=int(input("Enter your range="))
print(a,"\n")
print(b,"\n")
for i in range(r-2):
    c=a+b
    print(c,",")
    a=b
    b=c
