A, B, N = map(int, input().split())

def f(x):
    return (A*x)//B - A*(x//B)

if B > N:
    print(f(N))
elif B == N:
    print(f(N-1))
else:
    print(f(B-1))
