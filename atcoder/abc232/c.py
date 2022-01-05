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
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

from itertools import permutations

N,M = LI()
AB = LLI1(M)
CD = LLI1(M)

edge_t = [[False]*N for _ in range(N)]
edge_a = [[False]*N for _ in range(N)]

for a,b in AB:
    edge_t[a][b] = True
    edge_t[b][a] = True
for c,d in CD:
    edge_a[c][d] = True
    edge_a[d][c] = True
debug(edge_t=edge_t)
debug(edge_a=edge_a)

P = permutations(range(N))
for pat in P:
    #debug(pat=pat)
    ok = True
    for i in range(N):
        for j in range(i+1,N):
            if edge_t[i][j] != edge_a[pat[i]][pat[j]]:
                ok = False
                #debug(i=i, j=j, pati=pat[i], patj=pat[j])
    if ok:
        print('Yes')
        break
else:
    print('No')
