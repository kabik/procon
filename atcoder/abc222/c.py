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

N, M = LI()
A = LLSI(2*N)

res = [[0,i] for i in range(2*N)]

def janken(h1, h2):
    if h1 == 'G':
        if h2 == 'G': return 0
        if h2 == 'C': return 1
        if h2 == 'P': return -1
    if h1 == 'C':
        if h2 == 'G': return -1
        if h2 == 'C': return 0
        if h2 == 'P': return 1
    if h1 == 'P':
        if h2 == 'G': return 1
        if h2 == 'C': return -1
        if h2 == 'P': return 0

for i in range(M):
    order = sorted(res)
    #print(order)
    for k in range(N):
        a,b = order[2*k][1], order[2*k+1][1]
        #print(k, 2*k, 2*k+1, a,b, A[a][i], A[b][i])
        v = janken(A[a][i], A[b][i])
        if v == 1:
            res[a][0] -= 1
        elif v == -1:
            res[b][0] -= 1
for w,i in sorted(res):
    print(i+1)
