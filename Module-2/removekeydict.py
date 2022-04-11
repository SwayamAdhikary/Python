d={"PC":1,"Car":2,"Bike":3,"Tyre":4}
n=input("Enter item you want to delete=")
if n in d:
    del d[n]
print(d)