import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

M = A[N-1]
K = [False]*(M+1)
ans = 0
for i in range(N-1):
    a = A[i]
    if K[a]:
        continue
    if A[i+1] != a:
        ans += 1
    for i in range(a, M+1, a):
        K[i] = True
if not K[ A[N-1] ]:
    ans += 1
print(ans)
