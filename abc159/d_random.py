import random
import math

N = 10**5*2

print(N)

for _ in range(N):
    a = math.floor(random.random() * N)
    print(a, end=' ')
