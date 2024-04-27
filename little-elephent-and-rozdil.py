#205A

n=int(input())
l0=list(map(int,input().split()))
l1=sorted(l0)

if len(l1)==1:
    print(1)
elif l1[0]==l1[1]:
    print("Still Rozdil")
else:
    print(l0.index(l1[0])+1)