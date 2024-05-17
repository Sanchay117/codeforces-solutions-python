#350A

n,m=map(int,input().split())

correct = list(map(int,input().split()))
wrong = list(map(int,input().split()))

mx = max(correct)
mn = min(wrong)

if mx<mn:
    poss=False
    for i in correct:
        if 2*i <= mx:
            poss=True
            break

    if poss:
        print(mx)
    else:
        mx=2*mx
        if mx<mn:
            print(mx)
        else:
            print(-1)

else:
    print(-1)