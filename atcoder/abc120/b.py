a, b, k = map(int, input().split())

cnt = 0
ans = 0
for i in reversed(range(1,101)):
    if a % i == 0 and b % i == 0:
        cnt += 1
        ans = i
    if cnt == k:
        break
print(ans)
