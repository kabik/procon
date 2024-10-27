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
edges = [[] for _ in range(N+1)]

for i in range(N-1):
    u,v = LI()
    edges[u].append(v)
    edges[v].append(u)

if len(edges[1]) == 1:
    print(1)
    exit()
else:
    # debug(edges=edges)
    l = []
    for k in edges[1]:
        shown = set()
        shown.add(1)
        stack = [k]
        while stack:
            # debug(shown=shown, stack=stack)
            now = stack.pop()
            shown.add(now)
            for to in edges[now]:
                if to in shown: continue
                stack.append(to)

        l.append(len(shown)-1) # 1は除く
    l.sort(reverse=True)
    # debug(l=l)
    print(sum(l[1:])+1) # 1自体も消すので
