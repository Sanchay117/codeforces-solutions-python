#352B

n = int(input())

sequence = list(map(int, input().split()))

already_done = [0 for x in range(100001)]
positions = [[] for y in range(100001)]
out = []

for i in range(len(sequence)):
    x = sequence[i]
    positions[x].append(i)

ans=0

for x in sequence:
    if already_done[x] == 0:
        already_done[x] += 1
        pos = positions[x]
        d = 0
        if len(pos) > 1:
            if len(pos) == 2:
                d = pos[1] - pos[0]
            else:
                d = pos[1] - pos[0]
                for k in range(2, len(pos)):
                    if pos[k] - pos[k - 1] != d:
                        d = -1
        if d != -1:
            ans+=1
            out.append(str(x) + " " + str(d))

print(ans)

out.sort(key=lambda x: int(x[0:x.find(" ")]))
for z in out:
    print(z)