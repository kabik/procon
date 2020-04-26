import random

s = []
for _ in range(200000):
    s.append(str(random.randint(1,9)))
print(''.join(s))
