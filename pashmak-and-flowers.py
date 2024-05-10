#459B

n = int(input())
beauty = list(map(int, input().split()))

beauty.sort()

num_of_min,num_of_max=1,1

for i in range(1,len(beauty)):
    if beauty[i]==beauty[0]:
        num_of_min+=1
    else:
        break

for j in range(len(beauty)-2,-1,-1):
    if beauty[j]==beauty[-1]:
        num_of_max+=1
    else:
        break

ans2 = num_of_min*num_of_max

if beauty[0]==beauty[-1]:
    ans2=int((len(beauty)*(len(beauty)-1))/2)

ans1=(beauty[0]-beauty[-1])*-1

print(ans1,ans2)