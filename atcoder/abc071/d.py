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

N = II()
S1 = SI()
S2 = SI()

T1 = [S1[0]]
T2 = [S2[0]]
for i in range(1,N):
    if S1[i] != T1[-1]:
        T1.append(S1[i])
    if S2[i] != T2[-1]:
        T2.append(S2[i])

ans = 3
if T1[0] != T2[0]:
    ans *= 2
for i in range(1, len(T1)):
    if T1[i-1] == T2[i-1]:
        if T1[i] == T2[i]:
            ans *= 2
        else:
            ans *= 2
    else:
        if T1[i] == T2[i]:
            pass
        else:
            ans *= 3
    ans %= MOD
print(ans)
