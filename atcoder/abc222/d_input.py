import random

MAX = 3000
N = 3
A = [int(random.randint(1, MAX))]
B = [int(random.randint(A[0], MAX))]

for i in range(N-1):
    A.append( int(random.randint(A[-1], MAX)) )
    B.append( int(random.randint(max(A[-1],B[-1]), MAX)) )

print(N)
print(*A)
print(*B)
