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
P = list(map(float, input().split()))

T = [[0]*(N+1) for _ in range(N)]
T[0][0] = (1-P[0])
T[0][1] = P[0]
for i in range(N-1):
    for j in range(N):
        T[i+1][j]   += T[i][j] * (1-P[i+1])
        T[i+1][j+1] += T[i][j] * P[i+1]
    #debug(i=i, ti=T[i+1])
print(sum(T[N-1][N//2+1:]))
