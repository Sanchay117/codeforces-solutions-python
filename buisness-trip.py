#149A
k=int(input())
inp=list(map(int,input().split()))
inp.sort(reverse=True)

track=0
ans=0

for x in inp:
    if(track<k):
        track+=x
        ans+=1

if(k>track):
    print(-1)
else:
    print(ans)