#230A

s,n=list(map(int,input().split()))

dragons=[]

ans="YES"

for i in range(n):
    x,y=list(map(int,input().split()))
    dragons.append({"strength":x,"bonus":y})

dragons.sort(key=lambda x:x["strength"])

for i in dragons:
    if i["strength"]<s:
        s+=i["bonus"]
    else:
        ans="NO"

print(ans)