#433A

n=int(input())
apples=list(map(int,input().split()))

cnt_100,cnt_200=0,0

for i in apples:
    if i==100:
        cnt_100+=1
    else:
        cnt_200+=1

if (sum(apples)/2)%100==0 and n!=1:
    x=int(sum(apples)/2)
    y=0
    while y<x and cnt_200>int(cnt_200/2):
        cnt_200-=1
        y+=200
    if y==x:
        print("YES")
    else:
        y-=200
        if cnt_100>1:
            print("YES")
        else:
            print("NO")
else:
    print("NO")