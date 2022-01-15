from collections import defaultdict
import sys
from typing import DefaultDict

# sys.setrecursionlimit(10**6)
def debug(**kwargs): print(f'DEBUG: {kwargs}', file=sys.stderr)
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

N,Q = LI()
A = LI()

d = defaultdict(dict)
cnt = defaultdict(int)
for i,a in enumerate(A):
    d[a][cnt[a]+1] = i+1
    cnt[a] += 1
#debug(d=d)
#debug(cnt=cnt)

for _ in range(Q):
    x, k = LI()
    if x in d and k in d[x]:
        print(d[x][k])
    else:
        print(-1)
