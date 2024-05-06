#337A

n,m=list(map(int,input().split()))

pieces=list(map(int,input().split()))
pieces.sort()

min=pieces[n-1] - pieces[0]

for i in range(1,m-n+1):
    if pieces[i+n-1]-pieces[i]<min:
        min=pieces[i+n-1]-pieces[i]

print(min)