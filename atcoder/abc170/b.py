X, Y = map(int, input().split())

ans = 'No'
for i in range(X+1):
    if 2 * i + 4 * (X-i) == Y:
        ans = 'Yes'
print(ans)
