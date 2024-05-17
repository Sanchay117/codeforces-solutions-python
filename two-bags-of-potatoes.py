#239A

y, k, n = map(int, input().split())

k0=k

X = []

while k <= n:
    if k - y > 0:
        X.append(str(k - y))
    k += k0

if len(X) == 0:
    print(-1)
else:
    print(" ".join(X))
