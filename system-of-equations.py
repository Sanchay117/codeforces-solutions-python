#214A

n,m=list(map(int,input().split()))

ans=0

for i in range(0,m+1):
    b=i
    a=float(m-(b**2))
    if a.is_integer() and a>=0:
        if a**2 +b == n:
            ans+=1

print(ans)