#58A

s=input()
ind=-1
possible=True

for i in range(len(s)):
    if s[i]=="h":
        ind=i
        break

if ind==-1:
    print("NO")
else:
    ind_e=ind
    for i in range(ind, len(s)):
        if s[i]=="e":
            ind_e=i
            break
    if ind_e>ind:
        ind_l = ind_e
        for i in range(ind_e,len(s)):
            if s[i]=="l":
                ind_l=i
                break
        if ind_l>ind_e:
            ind_l2 = ind_l
            for i in range(ind_l+1,len(s)):
                if s[i]=="l":
                    ind_l2=i
                    break
            if ind_l2>ind_l:
                ind_o = ind_l2
                for i in range(ind_l2,len(s)):
                    if s[i]=="o":
                        ind_o=i
                        break
                if ind_o>ind_l2:
                    print("YES")
                else:
                    print("NO")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
