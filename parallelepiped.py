#224A

l=list(map(int,input().split()))


# we need a X b X c such that aXb=l[0] bXc=l[1] cXa=l[2]

a = ((l[0]*l[2])/l[1])**0.5
b = ((l[0]*l[1])/l[2])**0.5
c = ((l[1]*l[2])/l[0])**0.5

print(int(4*(a+b+c)))