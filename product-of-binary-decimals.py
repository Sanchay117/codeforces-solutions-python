#1950D Couln't solve without seeing solution code given here is incorrect

t=int(input())

for _ in range(t):
    n=int(input())

    while n>0:
        if n%10==0:
            n=n//10
        elif n%11==0:
            n=n//11
        elif n==1:
            print("YES")
            break
        else:
            print("NO")
            break
if n==0:
    print("YES")