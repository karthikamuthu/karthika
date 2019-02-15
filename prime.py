n=int(input())
flag=0
for i in range(2,n,-1):
	if n%1==0:
		flag=1
		break
if flag==0:
       print("prime")
else:
       print("not")# your code goes here
