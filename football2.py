#96A

inp=input()

prev=inp[0]
ans=1

for x in range(1,len(inp)):
    if ans>6:
        break
    if inp[x]==prev:
        ans+=1
    else:
        ans=1
    prev=inp[x]

if ans>6:
    print("YES")
else:
    print("NO")