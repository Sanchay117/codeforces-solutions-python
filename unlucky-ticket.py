#160B

n = int(input())
ticket = input()
ticket = [*ticket]

left = ticket[:n]
right = ticket[n:]

left = sorted(left)
right = sorted(right)

establishCriteria = 0 if left[0] > right[0] else 1
unlucky = True

if left[0]==right[0]:
    unlucky = False

if unlucky:
    for i in range(1, len(left)):
        criteria = 0 if left[i] > right[i] else 1
        if left[i]==right[i]:
            unlucky = False
            break
        if criteria != establishCriteria:
            unlucky = False
            break

print("YES" if unlucky else "NO")
