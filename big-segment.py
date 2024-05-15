#242B

n=int(input())

poss=True

mn=1000000000
mx=0

l0,r0=0,0

ind = -2

for i in range(n):
    l,r=list(map(int,input().split()))

    if i==0:
        mn=l
        mx=r
        l0,r0=l,r
    else:
        if l<=mn and r>=mx:
            ind=i
            mn=l
            mx=r
        elif l<mn:
            ind=-2
            mn=l
        elif r>mx:
            ind=-2
            mx=r


if mn==l0 and mx==r0:
    ind+=2

print(ind+1)
