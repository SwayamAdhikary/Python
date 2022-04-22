import csv
f=open(r'student.csv','r')
r=csv.reader(f)
for i in r:
    print(i)
    