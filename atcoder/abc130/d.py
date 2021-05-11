import bisect
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

S = [0]
sm = 0
for a in A:
    sm += a
    S.append(sm)

ans = 0
for i in range(N+1):
    r = bisect.bisect_left(S, K+S[i])
    if r <= K and N-r+1 > 0:
        ans += N-r+1
print(ans)
