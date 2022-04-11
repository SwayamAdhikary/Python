def gcd(a,b):
    if(b == 0):
        return a
    else:
        return gcd(b, a%b)

i,j=map(int,input("Enter your numbers =").split())
hcf=gcd(i,j)
print("GCD/HCF is=",hcf)
