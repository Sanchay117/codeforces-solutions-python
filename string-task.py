#118A

inp=input()
another=""
ano=""

for i in range(0,len(inp)):
    if inp[i] not in "AEIOUYaeiouy":
        another+=inp[i]

for i in range(0,len(another)):
    ano+="."
    if another[i] in "BCDFGHJKLMNPQRSTVWXZ":
        ano+=chr(ord(another[i])+32)
    else:
        ano+=another[i]
print(ano)
