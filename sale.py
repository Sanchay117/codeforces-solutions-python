#34B
n,m=list(map(int,input().split()))

ans=0
m_cnt=1
inp=list(map(int,input().split()))
inp.sort()
for x in inp:
    if x<0 and m_cnt<=m:
        m_cnt+=1
        ans+=abs(x)

print(ans)