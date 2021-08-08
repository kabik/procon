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

H, W, N = LI()
AB = LLI(N)
A = [a for a,b in AB]
B = [b for a,b in AB]
C = sorted(A)
D = sorted(B)

E = {}
now = -1
cnt = 0
for i in range(N):
    c = C[i]
    if c != now:
        cnt += 1
        now = c
    E[c] = cnt

F = {}
now = -1
cnt = 0
for i in range(N):
    d = D[i]
    if d != now:
        cnt += 1
        now = d
    F[d] = cnt
#print(E)
#print(F)

for a, b in AB:
    print(E[a], F[b])
