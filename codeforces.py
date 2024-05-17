t=int(input())

for i in range(t):
    n=int(input())
    chips=list(map(int,input().split()))

    cnt1=0
    for i in chips:
        if i==1:
            cnt1+=1

    if cnt1==1 or cnt1==n:
        print(0)
    else:
        ind=0
        for i in range(n-1):
            if chips[i]==1 and chips[i+1]==0:
                ind=i
                break
