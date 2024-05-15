#327B

n = int(input())

import math

seq = []

# Function to generate first n primes
for i in range(1000000, 1000000 + n):
    seq.append(i)

if n == 1:
    print(2)
else:
    for x2 in seq:
        print(x2, end=" ")
