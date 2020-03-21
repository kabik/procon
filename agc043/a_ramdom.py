import random

W = 100
H = 100

print(W, H)

for _ in range(H):
    s = ''
    for _ in range(W):
        if random.random() > 0.5:
            s = s + '.'
        else:
            s = s + '#'
    print(s)
