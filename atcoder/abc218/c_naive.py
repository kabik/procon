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

import numpy as np

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

def get_first(X):
    for i in range(N):
        for j in range(N):
            if X[i][j] == 1:
                return (i,j)

s_cnt = sum([sum(s) for s in S])
t_cnt = sum([sum(t) for t in T])
if s_cnt != t_cnt:
    print('No')
else:
    SA = np.array(S, dtype=np.int)
    TA = np.array(T, dtype=np.int)

    tx, ty = get_first(TA)
    ans = 'No'
    rot_a = SA
    for _ in range(4):
        rot_a = np.rot90(rot_a)
        for i in range(N):
            for j in range(N):
                a = np.roll(rot_a, (i,j), axis=(0,1))
                if np.array_equal(a, TA):
                    ans = 'Yes'
    print(ans)
