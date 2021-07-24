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

S = SI()

chokudai = 'chokudai'
d = dict(zip(chokudai, [0]*8))
ans = dict(zip(chokudai, [0]*8))
for c in S:
    if c in d:
        d[c] = (d[c]+1) % MOD
    else:
        continue
    idx = chokudai.index(c)
    if idx == 0:
        ans[c] = (ans[c]+1) % MOD
    else:
        ans[c] = (ans[c] + ans[chokudai[idx-1]]) % MOD
print(ans['i'])
