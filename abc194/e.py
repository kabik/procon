from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = Counter(A[:M])
ans = 0
while cnt[ans]:
    ans += 1

for i in range(M,N):
    cnt[A[i]] += 1
    cnt[A[i-M]] -= 1
    if cnt[A[i-M]] == 0:
        ans = min(ans, A[i-M])
print(ans)
