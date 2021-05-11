import random
import math

#N = 10**6
N = math.floor(random.random()*8)+2
s = ''
for _ in range(N):
    r = random.random()
    if r > 0.66:
        s = s + '1'
    elif r > 0.33:
        s = s + '2'
    else:
        s = s + '3'

print(N)
print(s)
