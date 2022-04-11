print("Select 1 for sum,2 for subtraction,3 for multiplication,4 for division, 5 for reaminder")
a=int(input("Enter your choice="))
x,y=map(int,input('enter you numbers=').split())
if a==1:
    print(x+y)
elif a==2:
    print(x-y)
elif a==3:
    print(x*y)
elif a==4:
    print(x/y)
elif a==5:
    print(x%y)
else:
    print('Select a correct option')
