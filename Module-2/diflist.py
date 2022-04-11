import math
l1=[]
l2=[]
s1=0
s2=0
n1=int(input("Enter length of l1="))
n2=int(input("Enter length of l2="))
for i in range(n1):
    a=int(input("Enter value in l1="))
    l1.append(a)
for j in range(n2):
    a=int(input("Enter value in l2="))
    l2.append(a)  
for k in range(n1):
     s1+=l1[k]
for l in range(n2):
    s2+=l2[l]    
print("Difference=",math.fabs(s1-s2))