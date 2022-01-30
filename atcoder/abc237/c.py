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
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

S = SI()
n = len(S)

start = 0
for i in range(n):
    if S[i] != 'a':
        break
    start = i+1

last = n
for i in range(n-1, -1, -1):
    if S[i] != 'a':
        break
    last = i

#T = S[start:last]
T = S[:last+start]
debug(T=T, Tinv=T[::-1])
if T == T[::-1]:
    print('Yes')
else:
    print('No')
