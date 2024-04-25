# 139A

n = int(input())
each_day = list(map(int, input().split()))
day = 0
ans = 0
while n > 0:
    n -= each_day[day % 7]
    day += 1
    ans = day%7 if day>7 else day
    if ans == 0:
        ans = 7

print(ans)
