import sys

# sys.setrecursionlimit(10**6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.buffer.readline())
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LI1(): return list(map(int1, sys.stdin.buffer.readline().split()))
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]
def BI(): return sys.stdin.buffer.readline().rstrip()
def SI(): return sys.stdin.buffer.readline().rstrip().decode()
def LSI(rows_number): return [SI() for _ in range(rows_number)]
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

N,K = LI()
if K == 0:
    print(N**2)
else:
    ans = 0
    for b in range(1, N+1):
        cand = max(0, b-K)
        period = (N+1)//b
        ans += cand * period
        ans += max(0, cand - (b - (N+1)%b))
    print(ans)
