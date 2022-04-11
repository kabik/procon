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
def LLSI(rows_number): return [SI() for _ in range(rows_number)]
def YN(b): print({True: 'Yes', False: 'No'}[b])
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

N = II()

ST = []
for _ in range(N):
    ST.append(LSI())

ok = True
for i in range(N):
    s_ok = True
    t_ok = True
    for j in range(N):
        if i == j: continue
        si, ti = ST[i]
        sj, tj = ST[j]
        if si == sj or si == tj:
            s_ok = False
        if ti == sj or ti == tj:
            t_ok = False
    if not s_ok and not t_ok:
        ok = False
YN(ok)
