#296A
import math

n = int(input())
arr = list(map(int, input().split()))

if n==1:
    print("YES")
else:
    counts = [0 for i in range(1000)]
    for i in arr:
        counts[i-1] += 1
    if max(counts)<=math.ceil(n/2):
        print("YES")
    else:
        print("NO")