#254A

f = open("input.txt", "r")

n = int(f.readline())
cards = list(map(int, f.readline()[:-1].split(' ')))

f.close()

pairs = []

inp = sorted(cards)
possible = True
for i in range(0, 2 * n, 2):
    if inp[i] != inp[i + 1]:
        possible = False
        break

if possible:
    yoyo = [ [] for _ in range(5000) ]
    for _ in range(2*n):
        card = cards[_]
        yoyo[card-1].append(_+1)


    for i in range(5000):
        if len(yoyo[i]) != 0:
            for j in range(0,len(yoyo[i]),2):
                pairs.append(str(yoyo[i][j])+" " + str(yoyo[i][j+1]))

f=open("output.txt","w")
if len(pairs) == 0 or not possible:
    f.write("-1")
else:
    for pair in pairs:
        f.write(pair + "\n")

f.close()
