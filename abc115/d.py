N, X = map(int, input().split())

A = [1]
P = [1]
for _ in range(N):
    A.append(2*A[-1] + 3 )
    P.append(2*P[-1] + 1 )

def f(n,x):
    v = -1
    if n == 0:
        v = P[0]
    elif x == 1:
        v = 0
    elif x <= A[n-1]+1:
        v = f(n-1, x-1)
    elif x == A[n-1]+2:
        v = P[n-1]+1
    elif x <= 2*A[n-1]+2:
        v = P[n-1] + 1 + f(n-1,x-A[n-1]-2)
    else:
        v = 2*P[n-1]+1
    return v

print(f(N,X))
