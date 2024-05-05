# contains random code for random problems i do on the fly
import math

n123 = int(input())

for i in range(n123):
    n,m=list(map(int,input().split()))
    a=input()
    b=input()
    l,r=0,0
    while l<len(a) and r<len(b):
        if a[l]==b[r]:
            l+=1
            r+=1
        else:
            r+=1


    print(l)
