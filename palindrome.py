n=int(input())
t=n
temp=0
while t!=0:
	temp=temp*10+t%10
	t=t//10
if n==temp:
		print("yes")
else:
        print("not")# your code goes here
