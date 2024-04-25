#43A

n=int(input())
teams=[]
names=[]

for i in range(n):
    s=input()
    if s not in names:
        names.append(s)
        teams.append({"name":s,"score":1})
    else:
        if teams[0]["name"]==s:
            teams[0]["score"]+=1
        else:
            teams[1]["score"]+=1
if len(teams)==1:
    print(teams[0]["name"])
else:
    x=max(teams[0]["score"],teams[1]["score"])
    if x==teams[0]["score"]:
        print(teams[0]["name"])
    else:
        print(teams[1]["name"])