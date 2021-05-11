N, X = map(int, input().split())
S = input()

ans = X
for c in S:
    if c == 'o':
        ans += 1
    else:
        ans = max(0, ans-1)
print(ans)
