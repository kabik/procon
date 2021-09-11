import random

N = int(random.randint(2, 5))

print(N)
for _ in range(2):
    for _ in range(N):
        for _ in range(N):
            k = random.randint(0,1)
            if k > 0:
                p = '#'
            else:
                p = '.'
            print(p, end='')
        print()
