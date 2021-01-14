N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for ab in AB:
    a, b = ab
    ans += b*(b+1)//2 - a*(a-1)//2
print(ans)
