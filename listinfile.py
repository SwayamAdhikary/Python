f=open(r'C:\Users\sadhi\OneDrive\Desktop\Python\Module-3\storye.txt','w')
l=eval(input("Enter list="))
for e in l:
    f.write(e+'\n')
f.close()