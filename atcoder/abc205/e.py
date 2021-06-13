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

N,M,K = LI()

def pow_mod(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow_mod(x * x % MOD, n // 2) % MOD
    else:
        return x * pow_mod(x * x % MOD, n // 2) % MOD

X = N+M+2
fact = [1]
for i in range(1,X+1):
    fact.append( (fact[i-1] * i) % MOD )
inv = [1] * (X+1)
inv[X] = pow_mod(fact[X], MOD-2)
for i in range(X, 1, -1):
    inv[i-1] = inv[i] * (i) % MOD

def cmb_mod(n,r):
    if n == r == 0:
        return 1
    elif n < r:
        return 0
    else:
        return fact[n] * inv[r] * inv[n-r] % MOD

if N <= M+K:
    ans = ( cmb_mod(N+M, N) - cmb_mod(N+M, M+K+1) ) % MOD
    print(ans)
else:
    print(0)
