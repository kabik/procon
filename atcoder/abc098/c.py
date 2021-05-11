N = int(input())
S = input()

r = 0
for c in S:
    if c == 'E':
        r += 1

ans = 10**10
for c in S:
    if c == 'E':
        r -= 1
        ans = min(ans, r)
    else:
        ans = min(ans, r)
        r += 1
print(ans)
