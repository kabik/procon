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
def YN(b): print({True: 'Yes', False: 'No'}[b])
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

C = LLI(3)

ans = 'Yes'
for i in range(2):
    if not (C[i][0] - C[i+1][0] == C[i][1] - C[i+1][1] == C[i][2] - C[i+1][2]):
        ans = 'No'
for j in range(2):
    if not (C[0][j] - C[0][j+1] == C[1][j] - C[1][j+1] == C[2][j] - C[2][j+1]):
        ans = 'No'
print(ans)
