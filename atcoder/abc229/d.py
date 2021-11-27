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
K = II()

N = len(S)
lb = [0]*N
rb = [0]*N
w_idx = []
M = 0
b = 0
for i in range(N):
    if S[i] == '.':
        w_idx.append(i)
        M+=1
        lb[i] = b
        b = 0
    else:
        b += 1
b = 0
for i in range(N-1, -1,-1):
    if S[i] == '.':
        rb[i] = b
        b = 0
    else:
        b += 1

if M == 0:
    print(N)
elif K == 0:
    print(max(max(lb), max(rb)))
elif K >= M:
    print(N)
else:
    ans = 0
    for i in range(M-K+1):
        l,r = w_idx[i], w_idx[i+K-1]
        ans = max(ans, r-l+1 +lb[l]+rb[r])
    print(ans)
