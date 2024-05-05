#208A

inp = input()
cnt = 0
ans = ""
while cnt < len(inp):
    if inp[cnt:cnt + 3] == "WUB":
        cnt += 3
    else:
        ind = -1
        for i in range(cnt, len(inp)):
            if inp[i:i + 3] == "WUB":
                ind = i
                break
        if ind == -1:
            ans+=inp[cnt:] + ' '
            break
        else:
            ans += inp[cnt:ind] + " "
        cnt += (ind - cnt)
ans = ans[:-1]
print(ans)
