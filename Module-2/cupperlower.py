from re import L


a=input('Enter your string=')
a.split()
cu=0
lc=0
sp=0
for i in a:
    if i.isupper():
        cu+=1
    elif i.islower():
        lc+=1
    else:
        sp+=1
print("Uppercase=",cu)
print("Lowercase=",lc)
print("Special=",sp)        