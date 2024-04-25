#34A

n = int(input())

height = list(map(int, input().split()))

min_height = abs(height[0] - height[1])
ind = 0

for i in range(n):
    if i == n - 1:
        if abs(height[n - 1] - height[0]) < min_height:
            min_height = abs(height[n - 1] - height[0])
            ind = i

    elif abs(height[i] - height[i + 1]) < min_height:
        min_height = abs(height[i] - height[i + 1])
        ind = i

if ind+1 == len(height):
    print(ind + 1, 1)
else:
    print(ind + 1, ind + 2)
