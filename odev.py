f=open(r'C:\Users\sadhi\OneDrive\Desktop\Python\Module-3\storye.txt','r+')
da=f.readline()
for i in da :
    j=int(i.strip())
    if j%2==0:
        f.write("Even=",j)
    else:
        f.write("Odd=",j)