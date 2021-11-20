def II(): return int(input())
def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

Q = II()
TX = LLI(Q)
N = 2**20
A = [-1]*N
P = [i for i in range(N)]

def find(par, x):
    if par[x] == x:
        return x
    par[x] = find(par, par[x])
    return par[x]

for t,x in TX:
    if t == 1:
        h = find(P, x%N)
        A[h] = x
        P[h] = find(P, (h+1)%N)
    else:
        print(A[x%N])
