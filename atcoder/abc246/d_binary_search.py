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

def f(a,b):
    return a*a*a + a*a*b + a*b*b + b*b*b

N = II()
x = 10**20
for a in range(10**6+1):
    ng, ok = -1, 10**6+1
    while ok - ng > 1:
        mid = (ng+ok)//2
        if f(a,mid) < N:
            ng = mid
        else:
            ok = mid
    b = ok
    if f(a,b) >= N:
        x = min(x, f(a,b))
print(x)
