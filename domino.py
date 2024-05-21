#353A

n = int(input())

lower = []
upper = []

for i in range(n):
    u, l = map(int, input().split())
    upper.append(u)
    lower.append(l)

if sum(lower) % 2 == 0 and sum(upper) % 2 == 0:
    print(0)
elif sum(lower) % 2 == 1 and sum(upper) % 2 == 1:
    possible = False
    for i in range(n):
        if (lower[i]%2==0 and upper[i]%2==1) or (lower[i]%2==1 and upper[i]%2==0):
            possible = True
            break
    print(1 if possible else -1)
else:
    print(-1)
