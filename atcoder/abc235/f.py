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

# 桁DP
N = SI()
M = II()
C = LI()

need = 0
for c in C:
    need |= 1<<c

nlen = len(N)
dpc, dps = [0]*(1<<10), [0]*(1<<10)
dp = [[[0]*2**10 for _ in range(2)] for _ in range(nlen+1)]
just = 0     # ピッタリN
just_cmb = 0 # ピッタリNに含まれる数字
for i in range(nlen):
    ndpc, ndps = [0]*(1<<10), [0]*(1<<10)
    ni = int(N[i])
    # 既にN以下が確定している場合
    for pat in range(1<<10):
        for dig in range(10):
            nxt = pat | (1<<dig)
            ndpc[nxt] += dpc[pat]
            ndps[nxt] += dps[pat] * 10 + dpc[pat] * dig

    # これ以前の桁が存在しない場合
    if i > 0:
        for dig in range(1, 10):
            nxt = 1<<dig
            ndpc[nxt] += 1
            ndps[nxt] += dig

    # これ以前の桁はNと一致するがここで一致しなくなる場合
    for dig in range(int(i==0), ni):
        nxt = just_cmb | (1<<dig)
        ndpc[nxt] += 1
        ndps[nxt] += just*10 + dig

    # MOD
    for pat in range(1<<10):
        dpc[pat] = ndpc[pat] % MOD
    for pat in range(1<<10):
        dps[pat] = ndps[pat] % MOD

    just = (just * 10 + ni) % MOD
    just_cmb |= 1 << ni

ans = 0
for pat in range(2**10):
    if (pat & need) == need:
        ans += dps[pat]
if (just_cmb & need) == need:
    ans += just
print(ans%MOD)
