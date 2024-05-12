#342A

n=int(input())

inp = list(map(int, input().split()))

ans=[]

cnt_1,cnt_2,cnt_3,cnt_4,cnt_5,cnt_6,cnt_7=0,0,0,0,0,0,0

for i in inp:
    match i:
        case 1:
            cnt_1+=1
        case 2:
            cnt_2+=1
        case 3:
            cnt_3+=1
        case 4:
            cnt_4+=1
        case 5:
            cnt_5+=1
        case 6:
            cnt_6+=1
        case 7:
            cnt_7+=1

if cnt_5>0 or cnt_7>0 or cnt_1!=(cnt_4+cnt_2+cnt_3+cnt_6):
    print(-1)
else:
    pass

#brain was fried knew the solution but as lazy cheated anyways...