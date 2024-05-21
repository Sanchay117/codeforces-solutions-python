#166A

def print_team(team):
    for x in team:
        print(x["problems"],x["penalty"])
    print("------------------------------")

n, k = map(int, input().split())

teams = []

for i in range(n):
    prob, penalty = map(int, input().split())
    teams.append({
        "problems": prob,
        "penalty": penalty
    })

teams.sort(key=lambda x: x["problems"], reverse=True)

i = 0
while i < len(teams):
    x = i
    for j in range(i + 1, n):
        if teams[j]["problems"] != teams[i]["problems"]:
            x = j
            break
    if teams[i]["problems"] == teams[n-1]["problems"]:
        srt = sorted(teams[i:], key=lambda xx: xx["penalty"])
        teams = teams[:i] + srt
        i = n
    elif x == i:
        i += 1
    else:
        srt = sorted(teams[i:x], key=lambda xx: xx["penalty"])
        teams = teams[:i] + srt + teams[x:]
        i = x


ans = 1
k_prob,k_penalty = teams[k-1]["problems"], teams[k-1]["penalty"]

for i in range(k-2,-1,-1):
    if teams[i]["problems"] == k_prob and teams[i]["penalty"] == k_penalty:
        ans += 1
    else:
        break

for i in range(k,n):
    if teams[i]["problems"] == k_prob and teams[i]["penalty"] == k_penalty:
        ans += 1
    else:
        break

print(ans)