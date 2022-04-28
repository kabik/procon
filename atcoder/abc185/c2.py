L = int(input())

ans = 1
for i in range(L-11,L):
    ans *= i
for i in range(1, 12):
    ans //= i
print(ans)
