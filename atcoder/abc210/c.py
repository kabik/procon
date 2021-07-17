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

N, K = LI()
C = LI()

d = {}
for i in range(K):
    if C[i] in d:
        d[C[i]] += 1
    else:
        d[C[i]] = 1

cnt = len(d)
ans = cnt
for i in range(1, N-K+1):
    d[C[i-1]] -= 1
    if d[C[i-1]] == 0:
        cnt -= 1

    if C[i+K-1] in d:
        d[C[i+K-1]] += 1
    else:
        d[C[i+K-1]] = 1
    if d[C[i+K-1]] == 1:
        cnt += 1
    ans = max(ans, cnt)
print(ans)
