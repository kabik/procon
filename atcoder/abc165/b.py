X = int(input())

k = 100
rate = 1.01

ans = 0
while k < X:
    k = k * rate // 1
    ans += 1
print(ans)
