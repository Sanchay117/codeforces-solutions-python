#1950B

t=int(input())

for i in range(t):
    n=int(input())

    alt2 = False
    for j in range(0,2*n,2):
        seq=""
        alt = alt2
        for k in range(0,2*n,2):
            if not alt:
                seq+="##"
            else:
                seq+=".."
            alt=not alt
        alt2=not alt2
        print(seq)
        print(seq)
