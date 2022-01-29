# ペア全列挙

import sys

def debug(**kwargs): print(f'DEBUG: {kwargs}', file=sys.stderr)
input = sys.stdin.buffer.readline
def II(): return int(input())
def LI(): return list(map(int, input().split()))

N = II()
M = N<<1
A = [0]*(1<<M)

for i in range(M-1):
    for j, score in enumerate(LI(), start=i+1):
        A[1<<i | 1 << j] = score

ans = 0
stack = [((1 << M) -1, 0)]
while stack:
    members, score = stack.pop()
    if members == 0:
        ans = max(ans, score)
        continue
    p1 = members & -members
    rest = members ^ p1
    while rest:
        p2 = rest & -rest
        rest = rest ^ p2
        stack.append((members^p1^p2, score^A[p1|p2]))
print(ans)
