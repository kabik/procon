import random

h = int(random.randint(2, 5))
w = int(random.randint(2, 5))
c = int(random.randint(1, 10))
A = [[int(random.randint(1, 1000)) for _ in range(w)] for _ in range(h)]

print(h, w, c)
for a in A:
    print(*a)
