N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort(key=lambda x: 2*x[0]+x[1], reverse=True)

aoki = sum(a for a,b in AB)
takahashi = 0
ans = 0
for a,b in AB:
    takahashi += a+b
    aoki -= a
    ans += 1
    if takahashi > aoki:
        break
print(ans)
