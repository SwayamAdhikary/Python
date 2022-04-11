import json
d={}
n=int(input('Enter your Range:'))
for i in range(1,n+1):
    d.update({i:i**2})
print(d)