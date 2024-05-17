#304A
n = int(input())
ans=0
for a in range(1,n):
    for b in range(a+1,n):
        c = (a**2 + b**2)**0.5
        if c.is_integer() and c<=n:
            ans+=1

print(ans)