#320 A

num=input()
ind=0
possible=True
while ind<len(num):
    if num[ind]=='1':
        if(ind==len(num)-1):
            break
        if  num[ind+1]=='1':
            ind+=1
        elif ind+2<len(num) and num[ind+2]=='4' and num[ind+1]=='4':
            ind+=3
        elif ind+1<len(num) and num[ind + 1]== '4':
            ind+=2
        else:
            ind+=1
    else:
        possible=False
        break
if possible:
    print("YES")
else:
    print("NO")
