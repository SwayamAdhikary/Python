import math
def ncr(n,r):
    a=math.factorial(n)
    b=math.factorial(r)
    c=math.factorial(n-r)
    return a//(b*c)
n=int(input('Enter the value of n:'))
r=int(input('Enter the value of r:'))
d=ncr(n,r)
print(d)

