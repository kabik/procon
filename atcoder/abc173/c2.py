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
def LLSI(rows_number): return [list(SI()) for _ in range(rows_number)]
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

from itertools import product
import copy

H,W,K = LI()
C = LLSI(H)

PH = list(product([0,1], repeat=H))
PW = list(product([0,1], repeat=W))

ans = 0
for ph in PH:
    for pw in PW:
        B = copy.deepcopy(C)
        for h in range(H):
            if ph[h]:
                for w in range(W):
                    B[h][w] = '-'
        for w in range(W):
            if pw[w]:
                for h in range(H):
                    B[h][w] = '-'
        cnt = 0
        for h in range(H):
            for w in range(W):
                if B[h][w] == '#':
                    cnt += 1
        if cnt == K:
            ans += 1
print(ans)
