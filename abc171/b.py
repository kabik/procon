import sys
input = sys.stdin.readline

N, K = map(int, input().split())
P = list(map(int, input().split()))
P.sort()

ans = 0
for i in range(K):
    ans += P[i]
print(ans)
