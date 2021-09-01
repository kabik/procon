N = int(input())
ST = [input().split() for _ in range(N)]
X = input()

ans = 0
for s,t in ST:
    ans += int(t)
    if s == X:
        ans = 0
print(ans)
