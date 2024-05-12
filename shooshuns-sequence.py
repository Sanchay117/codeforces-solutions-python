#222A

n, k = list(map(int, input().split()))

seq = list(map(int, input().split()))

possible = True

x = seq[0]
lala = True

for i in range(1, len(seq)):
    if seq[i] != x:
        lala = False
        break

if lala:
    print(0)
    exit(0)

for i in range(k, len(seq)):
    if seq[i] != seq[k - 1]:
        possible = False
        break

if not possible:
    print(-1)
else:
    ind = k - 2

    if seq[ind] != seq[k - 1]:
        print(k - 1)
    else:
        x = 0
        while ind > -1:
            if seq[ind] == seq[k - 1]:
                x += 1
            else:
                break
            ind -= 1
        print(k-1-x)
