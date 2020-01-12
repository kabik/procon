n, k, m = map(int, input().split())
a = list(map(int, input().split()))

sum = 0
for i in a:
    sum += i

diff = m * n - sum

if diff <= k and diff >= 0:
    print(diff)
elif diff <= k and diff < 0:
    print(0)
else:
    print(-1)
