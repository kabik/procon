N, M = map(int, input().split())
A = [int(input()) for _ in range(M)]
broken = set(A)
mod = 1000000007

unreachable = False
for i in range(M-1):
    if A[i+1] - A[i] == 1:
        unreachable = True
        break

pat = [0]*(N+2)
pat[0] = 1
if unreachable:
    print(0)
else:
    for i in range(N):
        if i in broken:
            continue
        pat[i+1] = (pat[i+1] + pat[i]) % mod
        pat[i+2] = (pat[i+2] + pat[i]) % mod
    print(pat[N])
