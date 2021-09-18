import random

N = int(random.randint(2, 5))
X = int(random.randint(1, 10))
Y = int(random.randint(1, 10))
A = [[int(random.randint(1, 10)) for _ in range(2)] for _ in range(N)]

print(N)
print(X, Y)
for a in A:
    print(*a)
