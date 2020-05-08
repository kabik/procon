import bisect

N = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        a,b = L[i], L[j]
        idx = bisect.bisect_left(L, a+b)
        ans += max(0, idx - j - 1)
print(ans)
