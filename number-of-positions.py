#124A

n,a,b=list(map(int,input().split()))

pos=list(range(1,n+1))

ans = 0
for x in pos:
    front = x-1
    bacc = len(pos)-x
    if front >= a and bacc <= b:
        ans += 1

print(ans)