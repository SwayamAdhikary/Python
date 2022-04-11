def pdt(x,y):

	if x < y:
		return pdt(y, x)
	elif y != 0:
		return (x + pdt(x, y - 1))
	else:
		return 0

x,y=map(int,input().split())
z=pdt(x, y)
print(z)



