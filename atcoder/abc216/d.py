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


N,M = LI()
inpath = [0] * N
outnode = [[] for i in range(N)]
for i in range(M):
    k = II()
    A = LI1()
    for i in range(k-1):
        a = A[i]
        na = A[i+1]
        outnode[a].append(na)
        inpath[na] += 1
S = []
L = []

for i in range(N):
    if inpath[i] == 0:
        S.append(i)

while S:
    k = S.pop()
    L.append(k)
    for i in outnode[k]:
        inpath[i] -= 1
        if inpath[i] == 0:
            S.append(i)

if len(L) != N:
    print('No')
else:
    print('Yes')
