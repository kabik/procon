N, M = map(int, input().split())
A = list(map(int, input().split()))

sm = sum(A)
if N < sm:
    print(-1)
else:
    print(N-sm)
