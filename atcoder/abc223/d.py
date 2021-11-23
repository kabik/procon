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

N, M = LI()
AB = LLI1(M)

inpath = [0] * N
outnode = [[] for _ in range(N)]
for a,b in AB:
    outnode[a].append(b)
    inpath[b] += 1
S = []
L = []

for i in range(N):
    if inpath[i] == 0:
        heappush(S, i)

while S:
    k = heappop(S)
    L.append(k)
    #print(k, L, S)
    for i in outnode[k]:
        #print(f'  {i}')
        inpath[i] -= 1
        if inpath[i] == 0:
            heappush(S, i)

if sum(inpath) > 0:
    print(-1)
else:
    L = map(lambda x: x+1, L)
    print(*L)
