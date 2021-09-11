import sys

# sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(input())
def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LI1(): return list(map(int1, input().split()))
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]
def BI(): return input().rstrip()
def SI(): return input().rstrip().decode()
def LSI(): return SI().split()
def LLSI(rows_number): return [SI() for _ in range(rows_number)]
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

#import numpy as np

N = II()
S = []
for _ in range(N):
    l = []
    for c in SI():
        if c == '#':
            l.append(1)
        else:
            l.append(0)
    S.append(l)
T = []
for _ in range(N):
    l = []
    for c in SI():
        if c == '#':
            l.append(1)
        else:
            l.append(0)
    T.append(l)

#SA = np.array(S, dtype=np.bool)
#TA = np.array(T, dtype=np.bool)

ans = 'No'

for w in [1,-1]:
    for y in [1,-1]:
        for i in range(N):
            for j in range(N):
                ok = True
                for x in range(N):
                    for y in range(N):
                        if
                if ok: ans = 'Yes'
print(ans)
