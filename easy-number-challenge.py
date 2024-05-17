#236B

a, b, c = map(int, input().split())

divisors = [0 for x in range(a*b*c)]

for x in range(a*b*c):
    num=x+1
    x0 = num

    while num<=(a*b*c):
        divisors[num-1]+=1
        num=num+x0

ans=0
for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            ans += divisors[i*j*k-1]

print(ans%1073741824)

