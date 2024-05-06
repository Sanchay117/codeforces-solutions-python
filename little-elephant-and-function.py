#221A

n=int(input())

a = [str(n)] + [str(x) for x in range(1,n)]
print(" ".join(a))