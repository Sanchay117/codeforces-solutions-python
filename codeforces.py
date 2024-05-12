# contains random code for random problems i do on the fly
import math

t = int(input())

for j in range(t):

    n, k, q = map(int, input().split())

    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))

    an = []

    for i in range(q):
        d = int(input())

        l, r = 0, k
        while l <= r:
            mid = (l + r) // 2
            if a[mid] > d:
                r = mid - 1
            else:
                l = mid + 1
        if a[r] == d:
            an.append(str(b[r]))
        else:
            y=round((a[r+1]-a[r])/(b[r+1]-b[r]),20)
            x=round(b[r] + ((d-a[r])/y),20)
            an.append(str(int(x)))

    print(" ".join(an))
