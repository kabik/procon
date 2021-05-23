import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ad = [0]*(N+1)
for i in range(N):
    ad[A[i]] += 1

ans = 0
for i in range(N):
    b = B[ C[i]-1 ]
    ans += ad[b]
print(ans)
