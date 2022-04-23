from email.policy import default
import sys

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
def LLSI(rows_number): return [list(SI()) for _ in range(rows_number)]
def YN(b): print({True: 'Yes', False: 'No'}[b])
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

import itertools
from collections import defaultdict

N, K = LI()
S = LLSI(N)

ans = 0
for select_num in range(K, N+1):
    for pat in itertools.combinations(S, select_num):
        cnt = defaultdict(int)
        for s in pat:
            for c in s:
                cnt[c] += 1
        t = [k for k in cnt if cnt[k] == K]
        ans = max(ans, len(t))
print(ans)
