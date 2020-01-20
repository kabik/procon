a, b = map(int, input().split())

t = 1
cnt = 0
while t < b:
    t = t - 1 + a
    cnt += 1

print(cnt)
