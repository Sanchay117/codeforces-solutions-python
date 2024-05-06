#218B

passengers, planes = list(map(int, input().split()))

empty_seats = list(map(int, input().split()))
emp = empty_seats.copy()
empty_seats.sort()

mn = 0

for x in range(passengers):
    mn+=empty_seats[0]
    empty_seats[0]-=1
    if empty_seats[0] == 0:
        empty_seats=empty_seats[1:]

emp.sort(reverse=True)

mx=0

for x in range(passengers):
    mx+=emp[0]
    emp[0]-=1
    if emp[0] == 0:
        emp=emp[1:]
    emp.sort(reverse=True)

print(mx,mn)