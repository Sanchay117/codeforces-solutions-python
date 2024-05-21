#349A

n = int(input())
change = list(map(int, input().split()))

poss = True

denominations = [0, 0, 0]  # 0 index for 25 ruble bill , 1 for 50 , 2 for 100

for changa in change:
    if changa == 25:
        denominations[0] += 1
    elif changa == 50:
        denominations[1] += 1
        if denominations[0] == 0:
            poss = False
            break
        else:
            denominations[0] -= 1
    else:
        denominations[2] += 1
        if denominations[1] == 0:
            if denominations[0] < 3:
                poss = False
                break
            else:
                denominations[0] -= 3
        else:
            if denominations[0] == 0:
                poss = False
                break
            else:
                denominations[1] -= 1
                denominations[0] -= 1

print("YES" if poss else "NO")
