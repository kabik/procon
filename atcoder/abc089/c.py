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

import collections
import itertools

N = II()
S = LLSI(N)

T = [s[0] for s in S]
ctr = collections.Counter(T)
l = []
for c in 'MARCH':
    if ctr.get(c):
        l.append(ctr.get(c))
    else:
        l.append(0)

ans = 0
for p in itertools.combinations(l, 3):
    ans += p[0] * p[1] * p[2]
print(ans)
