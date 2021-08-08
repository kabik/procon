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

N = II()
AB = LLI1(N-1)

edge = [ [] for _ in range(N) ]
for a,b in AB:
    edge[a].append( b )
    edge[b].append( a )
q = [ [] for _ in range(N) ]
for i in range(N):
    for e in set(edge[i]):
        heappush(q[i], e)

first = [-1]*N
first[0] = 10**10
from_idx = 0
while True:
    print(from_idx+1, end=' ')
    while q[from_idx]:
        to_idx = heappop(q[from_idx])
        if first[to_idx] >= 0:
            continue
        else:
            if first[to_idx] < 0:
                first[to_idx] = from_idx
            from_idx = to_idx
            break
    else:
        if from_idx == 0:
            break
        else:
            from_idx = first[from_idx]
print()
