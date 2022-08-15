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
INF = 10 ** 40
MOD = 10 ** 9 + 7
# MOD = 998244353

X, A, D, N = LI()

if D < 0:
    D = -D
    X = -X
    A = -A

def val(i):
    return A + (i-1)*D

ng, ok = 0, N
while ok-ng > 1:
    m = (ng + ok) // 2
    debug(ng=ng, ok=ok, m=m)
    if val(m) < X:
        ng = m
    elif val(m) > X:
        ok = m
    else:
        print(0)
        exit(0)
debug(ok=ok)

if ok > 1:
    print(min( abs(val(ok)-X), abs(val(ng)-X) ))
else:
    print(abs(val(ok)-X))
