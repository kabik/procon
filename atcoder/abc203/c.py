N,K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort()

now = 0
for i in range(N):
    a,b = AB[i]
    if K < a-now:
        now += K
        K = 0
        break
    else:
        K -= a-now
        K += b
        now = a
if K > 0:
    now += K
print(now)
