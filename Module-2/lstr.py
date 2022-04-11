s=eval(input("Enter list of string="))
c=0
for i in s:
    for j in range(len(i)):
        if len(i)>=2 and s[0]==s[-1]:
            c+=1
print(c)            
