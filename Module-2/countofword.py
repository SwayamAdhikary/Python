str =input("Enter string=")
word =input('Enter counted=')
a = str.split(" ")
count = 0
for i in range(0, len(a)):
		if (word == a[i]):
		    count = count + 1
			
print(count)	
