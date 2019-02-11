n=int(input())
x=list(map(int,input().split()))
m=1
for i in  range (1,n):
    if x[i]<m:
        x[i]=m
print (m)
