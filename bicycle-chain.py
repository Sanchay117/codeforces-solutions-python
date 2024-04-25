#215A

n=int(input())
a_i=list(map(int,input().split()))
m=int(input())
b_i=list(map(int,input().split()))

ans=0
max=0

l=[]

if n>m:
    for x in range(n):
        for y in range(m):
            if (b_i[y]/a_i[x]).is_integer():
                if(b_i[y]/a_i[x])>max:
                    max=b_i[y]/a_i[x]
                l.append(b_i[y]/a_i[x])
else:
    for y in range(m):
        for x in range(n):
            if (b_i[y]/a_i[x]).is_integer():
                if(b_i[y]/a_i[x])>max:
                    max=b_i[y]/a_i[x]
                l.append(b_i[y]/a_i[x])

print(l.count(max))
