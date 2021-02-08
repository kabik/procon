import bisect

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_SUM = [0]
for a in A:
    A_SUM.append(A_SUM[-1] + a)
B_SUM = [0]
for b in B:
    B_SUM.append(B_SUM[-1] + b)

ans = 0
for i in range(N+1):
    if A_SUM[i] <= K:
        l = bisect.bisect_right(B_SUM, K-A_SUM[i]) -1
        ans = max(ans, l+i)
print(ans)
