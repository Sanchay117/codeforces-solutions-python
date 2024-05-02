#352A

n=int(input())
digits=list(map(int,input().split()))

if 0 not in digits:
    print(-1)
else:
    cntOf5=0
    for digit in digits:
        if digit == 5:
            cntOf5+=1
    cntOf0=len(digits)-cntOf5
    found=False
    for x in range(cntOf5,0,-1):
        if (5*x)%9==0:
            print("5"*x + "0"*cntOf0)
            found=True
            break
    if not found:
        print(0)