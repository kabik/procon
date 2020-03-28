import math

N = int(input())

ans = 10**15
for k in range(1, int(math.sqrt(N))+1):
    if N % k > 0:
        continue
    ans = min(ans, k + N//k - 2)
print(ans)
