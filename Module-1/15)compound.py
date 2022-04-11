p=float(input("Enter your principal amount="))
r=float(input("Enter your rate of interest="))
t=int(input("Enter your time="))
r=p*(1+(r/100))
for i in range(2,t+1):
       r=r*(1+(r/100))
print("Value=",r)       