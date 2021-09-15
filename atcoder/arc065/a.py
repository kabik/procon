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

np,mp = 1,1
for i in range(1,N+1):
    np = (np*i) % MOD
for i in range(1,M+1):
    mp = (mp*i) % MOD

if abs(N-M) > 1:
    print(0)
elif abs(N-M) == 1:
    print( (np*mp)%MOD )
else:
    print( (np*mp*2)%MOD )
