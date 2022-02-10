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
#MOD = 10 ** 9 + 7
MOD = 998244353

def f(x):
    return x*(x+1)//2

N = II()

if N < 10:
    print(N*(N+1)//2)
else:
    ans = 45
    k = 10
    while k*10 <= N:
        ans += f(k*10 - k)
        ans %= MOD
        k *= 10
    ans += f(N-k+1)
    ans %= MOD
    print(ans)
