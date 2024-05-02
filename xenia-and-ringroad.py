#339B

n,m = list(map(int,input().split()))

task=list(map(int,input().split()))

ans=0
crntHose = 1
for x in task:
    if x<crntHose:
        ans+=(n-crntHose)+x
    else:
        ans+= x - crntHose
    crntHose = x

print(ans)