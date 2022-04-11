print("Select 1 for time conversion 2 for distance 3 for temperature")
a=int(input("Enter your choice="))
if a==1:
    b=int(input("Enter time in hours="))
    print("Time in minutes=",b*60)
elif a==2:
    b=int(input("Enter distance in kilometers="))
    print("Distance in miles=",b*1.6)
elif a==3:
    b=int(input("Enter temperature in celcius="))
    print("Temperature in farenheit=",(1.8*b)+32)
else:
    print("Enter a correct choice")            