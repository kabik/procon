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

HW = LI()
H, W = HW[:3], HW[3:]
MAX = max(HW)

ans = 0
for h0w0 in range(1,MAX+1):
    for h1w0 in range(1,MAX+1):
        for h0w1 in range(1,MAX+1):
            for h1w1 in range(1,MAX+1):
                h0w2 = H[0] - h0w0 - h0w1
                h1w2 = H[1] - h1w0 - h1w1
                h2w0 = W[0] - h0w0 - h1w0
                h2w1 = W[1] - h0w1 - h1w1
                h2w2 = W[2] - h0w2 - h1w2
                if h0w2 > 0 and h1w2 > 0 and h2w0 > 0 and h2w1 > 0 and h2w2 > 0 and h2w0 + h2w1 + h2w2 == H[2]:
                    ans += 1
                    # print(h0w0, h0w1, h0w2)
                    # print(h1w0, h1w1, h1w2)
                    # print(h2w0, h2w1, h2w2)
                    # print()
print(ans)
