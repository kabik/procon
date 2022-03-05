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

S = SI()
Q = II()
TK = LLI(Q)

N=len(S)
d = {'A':'BC', 'B':'CA', 'C':'AB'}

def leaf(origin, rest, t):
    if t == 0:
        return origin
    else:
        cand = leaf(origin, rest//2, t-1)
        return d[cand][rest%2]

for t,k in TK:
    k-=1
    if t>60:
        origin = S[0]
        ans = leaf(origin, k, 60+t%3)
        print(ans)
    else:
        orig_idx = k//(2**t)
        origin = S[orig_idx]
        ans = leaf(origin, k%(2**t), t)
        print(ans)
