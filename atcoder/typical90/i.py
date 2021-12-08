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
CP = LLI(N)
Q = II()
LR = LLI1(Q)

S1 = [0]*N
S2 = [0]*N
if CP[0][0] == 1:
    S1[0] = CP[0][1]
else:
    S2[0] = CP[0][1]
for i in range(1,N):
    c,p = CP[i]
    S1[i] = S1[i-1]
    S2[i] = S2[i-1]
    if c == 1:
        S1[i] += p
    else:
        S2[i] += p

for l, r in LR:
    if l == 0:
        print( S1[r], S2[r] )
    else:
        print( S1[r]-S1[l-1], S2[r]-S2[l-1] )
