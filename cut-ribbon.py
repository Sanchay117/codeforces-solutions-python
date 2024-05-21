#189A

n, a, b, c = map(int, input().split())

mx = 0

for i in range(0,n):
    for j in range(0,n):
        k = (n-(j*b+i*a))/c
        if k.is_integer() and i+j+k>mx:
            mx = i+j+k

print(int(mx))