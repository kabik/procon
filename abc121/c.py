N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort()

sum = 0
cnt = 0
for ab in AB:
    a,b = ab[0], ab[1]
    if cnt + b < M:
        sum += a * b
        cnt += b
    else:
        sum += a * (M-cnt)
        break
print(sum)
