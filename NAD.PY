n,a,d=map(int,input().split())
i=1
ap=0
while i<=n:
    ap=ap+a
    a=a+d
    i=i+1
print(ap)
