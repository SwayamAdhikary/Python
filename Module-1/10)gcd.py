a,b=map(int, input("Enter the numbers=").split())
if a>b & a%b==0:
        print(b,"Is the gcd")
elif b>a & b%a==0:
        print(a,"Is the gcd")
elif a==b:
        print(a,"Is the gcd")
else:
    if a>b:
        for i in range(a):
            if i%b==0:
                print("GCD=",i)
    else:
        for i in range(b):
            if i%a==0:
                print("GCD=",i)                    
