n = int(input())
a = [int(input()) for _ in range(n)]

m, m2 = 0,0
for ai in a:
    if ai > m:
        m, m2 = ai, m
    elif ai > m2:
        m2 = ai

for ai in a:
    if ai == m:
        print(m2)
    else:
        print(m)
