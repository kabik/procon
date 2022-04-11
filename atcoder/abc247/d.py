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

Q = II()

now = 0
l = []
for _ in range(Q):
    q = LI()
    if q[0] == 1:
        x, c = q[1:]
        l.append([x,c])
    else:
        c = q[1]
        ans = 0
        while c:
            k, cnt = l[now]
            minus = min(c, cnt)
            #debug(k=k, cnt=cnt, c=c)
            ans += minus*k
            l[now][1] -= minus
            if l[now][1] == 0:
                now += 1
            c -= minus
        print(ans)
