import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

m = 0
ans = [0]*N
for i in range(N, 0, -1):
    a = A[i-1]
    cnt = 0
    for k in range(i+i, N+1, i):
        cnt += ans[k-1]
    if a != cnt % 2:
        ans[i-1] = 1
        m += 1

print(m)
for i in range(N):
    if ans[i] > 0:
        print(i+1, end=' ')
print()
