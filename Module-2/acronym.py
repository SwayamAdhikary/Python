a=input("Enter your string=")
b=''
for i in range(len(a)):
    if i==0:
        b=b+a[i].capitalize()
    elif a[i]==' ':
        b=b+a[i+1].capitalize()
print(b)        