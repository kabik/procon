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
def LLSI(rows_number): return [SI().split() for _ in range(rows_number)]
def YN(b): print({True: 'Yes', False: 'No'}[b])
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

from collections import defaultdict

N = II()
ST = LLSI(N)

orgs = []
P = defaultdict(int)
for i in range(N):
    s, _t = ST[i]
    t = int(_t)
    if s not in P:
        orgs.append((s,t,i+1))
    P[s] = max(P[s], t)

m = -1
for o in orgs:
    m = max(m, o[1])

for o in orgs:
    if o[1] == m:
        print(o[2])
        break
