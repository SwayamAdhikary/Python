a,b,c,d,e=map(int, input("Enter marks of subject respectively=-").split())
if (a+b+c+d+e)/5>=90:
    print("A+")
elif (a+b+c+d+e)/5>=80 and (a+b+c+d+e)/5<90:
    print("A")
else:
    print("Try Hard")        