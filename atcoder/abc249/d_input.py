import random

N = int(random.randint(2, 10)) # 2 <= h <= 5
A = [int(random.randint(1, 10)) for _ in range(N)]

print(N)
print(*A)
