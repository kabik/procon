import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

sm = 0
d = {}
for a in A:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
    sm += a

for _ in range(Q):
    b, c = map(int, input().split())
    if b in d:
        sm += (c-b) * d[b]
        if c in d:
            d[c] += d[b]
        else:
            d[c] = d[b]
        d.pop(b)
    print(sm)
