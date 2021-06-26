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
TLR = LLI(N)
TLR.sort(key=lambda x: (x[1],x[0]))

ans = 0
for i in range(N):
    #print(TLR[i])
    ti,li,ri = TLR[i]
    for j in range(i+1, N):
        tj,lj,rj = TLR[j]
        if lj < ri:
            ans += 1
        elif lj == ri and ti in [1,3] and tj in [1,2]:
            ans += 1
print(ans)
