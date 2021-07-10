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

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, Q = LI()
edge = [ [] for _ in range(N) ]
for _ in range(N-1):
    a,b = LI()
    edge[a-1].append( (1, b-1) )
    edge[b-1].append( (1, a-1) )

INF = 10**15
dist = [INF]*N
dist[0] = 0
q = [(0,0)]
while q:
    now, from_idx = heappop(q)
    if now > dist[from_idx]: continue
    for d, to_idx in edge[from_idx]:
        t = now + d
        if t >= dist[to_idx]: continue
        dist[to_idx] = t
        heappush( q, (dist[to_idx], to_idx) )

for _ in range(Q):
    c,d = LI()
    c -= 1
    d -= 1
    if (dist[c] - dist[d]) % 2 == 0:
        print('Town')
    else:
        print('Road')
