#431B
from itertools import permutations

combinations = list(permutations(range(1, 6)))

for i in range(len(combinations)):
    s = ""
    for j in combinations[i]:
        s += str(j)
    combinations[i] = s

happi = []
for i in range(5):
    happi.append(list(map(int, input().split())))

mx = []

for combination in combinations:
    a, b, c, d, e = combination
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    x = happi[a - 1][b - 1] + happi[b - 1][a - 1] + happi[c - 1][d - 1] + happi[d - 1][c - 1] + happi[b - 1][c - 1] + \
        happi[c - 1][b - 1]
    x += happi[d - 1][e - 1] + happi[e - 1][d - 1] + happi[c - 1][d - 1] + happi[d - 1][c - 1] + happi[d - 1][e - 1] + \
         happi[e - 1][d - 1]
    mx.append(x)

print(max(mx))
