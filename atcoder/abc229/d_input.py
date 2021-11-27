import random

N = int(random.randint(10, 20))
K = int(random.randint(10, 20))

s = []
for _ in range(N):
    if int(random.randint(0, 1)) == 0:
        s.append('.')
    else:
        s.append('X')

print(''.join(s))
print(K)
