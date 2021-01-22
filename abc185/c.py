L = int(input())

ans = 1
for i in range(11):
    ans *= L-1-i
for i in range(1, 12):
    ans //= i
print(ans)
