#43B

h=input()
txt=input()

poss=True

for x in txt:
    if x!=" ":
        cnt_x=0
        cnt_x_in_h=0
        for z in txt:
            if x==z:
                cnt_x+=1
        for y in h:
            if y==x:
                cnt_x_in_h+=1
        if cnt_x>cnt_x_in_h:
            poss=False
            break

if poss:
    print("YES")
else:
    print("NO")