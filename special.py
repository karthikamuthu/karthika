n=input()
a=b=c=0
for i in range(0,len(n)):
	if n[i].isalpha():
		a=a+1
		if n[i].isnumeric():
		 	b=b+1
		else:
		 	c=c+1
print(c)		
		
