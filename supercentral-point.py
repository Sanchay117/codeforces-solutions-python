# 165A

n = int(input())
points = []
for i in range(n):
    inp = list(map(int, input().split()))
    points.append(inp)
ans = 0

for x, y in points:
    left, right, top, down = False, False, False, False

    for x_dash, y_dash in points:
        if y == y_dash and x_dash > x:
            left = True
        if y == y_dash and x_dash < x:
            right = True
        if x == x_dash and y_dash > y:
            top = True
        if x == x_dash and y_dash < y:
            down = True

    if left and right and top and down:
        ans += 1

print(ans)