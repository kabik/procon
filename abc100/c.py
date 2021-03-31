N = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    while a % 2 == 0:
        ans += 1
        a //= 2
print(ans)
