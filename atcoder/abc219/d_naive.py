from itertools import repeat
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

N = II()
X, Y = LI()
AB = LLI(N)

a_sum = sum([a for a,_ in AB])
b_sum = sum([b for _,b in AB])
if a_sum < X or b_sum < Y:
    print(-1)
else:
    from itertools import product

    ans = INF
    for pat in product([0,1], repeat=N):
        x,y = 0,0
        for i, p in enumerate(pat):
            if p == 1:
                a,b = AB[i]
                x += a
                y += b
        if x >= X and y >= Y:
            ans = min(ans, sum(pat))
    print(ans)
