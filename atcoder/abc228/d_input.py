import random

Q = int(random.randint(50, 100))
TX = [[int(random.randint(1, 2)), int(random.randint(0, 10**18))] for _ in range(Q)]

print(Q)
for t,x in TX:
    print(t,x)
