n=int(input())
x=list(map(int,input().split()))
m=0
for i in range(0,n):
    if x[i]>m:
      m=x[i]
print (m)

    
