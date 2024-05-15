#186A

s1 = input()
s2 = input()

possible = True


def swap(st, a_ind, b_ind):
    if a_ind == b_ind:
        return st
    if a_ind > b_ind:
        tmp = a_ind
        a_ind = b_ind
        b_ind = tmp
    return st[:a_ind] + st[b_ind] + st[a_ind + 1:b_ind] + st[a_ind] + st[b_ind + 1:]


l, r = 0, 0

while l < len(s1) and r < len(s2):
    if swap(s1, l, r) == s2:
        break
    if s1[l] == s2[r] and l == r:
        l += 1
        r += 1
    else:
        l += 1

if l == len(s1) or len(s1)!=len(s2):
    possible = False

if not possible:
    print("NO")
else:
    print("YES")