#363B

n, k = map(int, input().split())

heights = list(map(int, input().split()))

res=[heights[0]]

for i in range(1, n):
    res.append(heights[i]+res[i-1])

i = 1

mn = res[k - 1]
ans = 0

while i < n - k + 1:
    if res[k + i-1] - res[i-1] < mn:
        mn = res[k + i-1] - res[i-1]
        ans = i
    i += 1

print(ans + 1)
