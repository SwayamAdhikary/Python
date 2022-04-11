n=int(input("Enter length of list="))
l=[]
max=-9999999
min=99999999
for i in range(n):
    a=int(input('Enter values into list='))
    l.append(a)    
for j in range(n):
    if l[j]>max:
        max=l[j]
    if l[j]<min:
        min=l[j]
for k in range(l.count(max)):       
        l.remove(max)
for m in range (l.count(min)):
        l.remove(min)
l.sort()
print(l[-1])        
print((l[0]))