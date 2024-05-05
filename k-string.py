#219A

k=int(input())
inp=input()

counts=[0]*26

def remove_items(test_list, item):
    # remove the item for all its occurrences
    c = test_list.count(item)
    for i in range(c):
        test_list.remove(item)
    return test_list

for i in inp:
    counts[ord(i)-97]+=1

possible = True

res=remove_items(counts.copy(),0)
for i in res:
    if i%k!=0:
        possible=False

if not possible:
    print(-1)
else:
    st=""
    for i in range(26):
        if counts[i]>0:
            st+=(chr(i+97))*(int(counts[i]/k))

    st*=k
    print(st)