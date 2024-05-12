#298B

t,s_x,s_y,e_x,e_y=list(map(float,input().split()))

wind=input()
time=0

for x in wind:

    if s_x<e_x and x=="E":
        s_x+=1
    elif s_x>e_x and x=="W":
        s_x-=1

    if s_y<e_y and x=="N":
        s_y+=1
    elif s_y>e_y and x=="S":
        s_y-=1

    time+=1

    if s_x==e_x and s_y==e_y:
        break

if s_x==e_x and s_y==e_y:
    print(time)
else:
    print(-1)