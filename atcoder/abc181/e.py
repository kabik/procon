import bisect
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))

if N == 1:
    ans = 10**20
    for w in W:
        ans = min(ans, abs(H[0]-w))
    print(ans)
else:
    H.sort()
    diff_sum = []
    diff_sum.append(H[1] - H[0])
    diff_sum.append(H[2] - H[1])
    for i in range(3,N):
        diff_sum.append(H[i]-H[i-1] + diff_sum[i-2-1])

    ans = 10**20
    for w in W:
        idx = bisect.bisect_right(H, w)
        if idx < 2:
            d = diff_sum[N-2] + abs(w-H[0])
        elif idx >= N-1:
            d = diff_sum[N-3] + abs(w-H[N-1])
        elif idx & 1: # odd
            d = diff_sum[idx-3] + w-H[idx-1] + diff_sum[N-2] - diff_sum[idx-2]
        else: # even
            d = diff_sum[idx-2] + H[idx]-w + diff_sum[N-2] - diff_sum[idx-1]
        ans = min(ans, d)
    print(ans)
