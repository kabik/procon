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

H, W, C = LI()
A = LLI(H)

ans = INF
for h1 in range(H):
    for w1 in range(W):
        for h2 in range(H):
            for w2 in range(W):
                if h1==h2 and w1==w2: continue
                ans = min(ans, A[h1][w1] + A[h2][w2] + C*(abs(h1-h2)+abs(w1-w2)))
print(ans)
