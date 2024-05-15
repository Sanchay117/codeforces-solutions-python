#258A

inp=input()
ind=-1

for i in range(0,len(inp)):
    if inp[i]=='0':
        ind=i
        break

if ind==-1:
    print(inp[1:])
else:
    print(inp[:ind]+inp[ind+1:])