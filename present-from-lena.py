#118B

n = int(input())
mx = 2*n + 1

print(" "*int((mx-1)/2)*2 + "0")

spaces = int(((mx-1)/2)*2)-2
for i in range(1,n):
    seq=[str(x) for x in range(i+1)] + [str(y) for y in range(i-1,-1,-1)]
    seq=" ".join(seq)
    print((" "*spaces)+seq)
    spaces-=2

print(" ".join([str(x) for x in range(n+1)] + [str(y) for y in range(n-1,-1,-1)]))

spaces = 2
for i in range(n-1,0,-1):
    seq=[str(x) for x in range(i+1)] + [str(y) for y in range(i-1,-1,-1)]
    seq=" ".join(seq)
    print((" "*spaces)+seq)
    spaces+=2

print(" "*int((mx-1)) + "0")