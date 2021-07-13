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
S = LLSI(N)

rev_edge = {}
cnt = {}
ans = {}
for s in S:
    head, tail = s[:3], s[-3:]
    rev_edge[head] = []
    rev_edge[tail] = []
    cnt[head] = 0
    cnt[tail] = 0
    ans[head] = -1
    ans[tail] = -1
for s in S:
    head, tail = s[:3], s[-3:]
    rev_edge[tail].append(head)
    cnt[head] += 1

q = []
for s in S:
    head, tail = s[:3], s[-3:]
    if cnt[tail] == 0:
        q.append(tail)
        ans[tail] = 0
while q:
    t = q.pop()
    for x in rev_edge[t]:
        if ans[x] == -1:
            cnt[x] -= 1
            if ans[t] == 0:
                ans[x] = 1
                q.append(x)
            elif cnt[x] == 0:
                ans[x] = 0
                q.append(x)

for s in S:
    head, tail = s[:3], s[-3:]
    if   ans[tail] == -1: print('Draw')
    elif ans[tail] == 0:  print('Takahashi')
    else:                 print('Aoki')
