#253A

f = open("input.txt", "r")

n,m=map(int,f.readline().split())
f.close()


st=""
alt = True if n>m else False
while n>0 and m>0:
    if not alt:
        st+="G"
        m=m-1
    else:
        st+="B"
        n=n-1
    alt = not alt

if n>0:
    st+="B"*n

if m>0:
    st+="G"*m

f = open("output.txt", "w")
f.write(st)
f.close()